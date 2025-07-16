import re
import os

def generate_moc_text(moc_file_path, output_file_path, main_notes_dir):
    """
    Generates a text file from an MOC, including content of linked notes
    and collecting sources, while excluding specific sections.
    """
    all_sources = set()
    processed_notes_content = {}
    added_note_titles_to_output = {} # To prevent adding the same note content multiple times

    # --- Phase 1: Pre-process All Main Notes ---
    for filename in os.listdir(main_notes_dir):
        if filename.endswith(".md"):
            note_full_name = filename[:-3] # Remove .md extension
            note_path = os.path.join(main_notes_dir, filename)

            try:
                with open(note_path, 'r', encoding='utf-8') as n_f:
                    note_content_raw = n_f.read()

                current_note_content = note_content_raw

                # 1. Remove YAML front matter (block starting and ending with ---)
                current_note_content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', current_note_content, flags=re.DOTALL | re.MULTILINE)

                # 2. Remove tags line if present (e.g., "Tags: #tag1, #tag2")
                current_note_content = re.sub(r'^Tags:.*$\n', '', current_note_content, flags=re.MULTILINE | re.IGNORECASE)

                # 3. Extract and remove Sources section, collecting sources
                # Match any level of heading for Sources
                sources_section_pattern = r'(?s)(^#+\s*Sources\s*\n)(.*?)(?=\n#+\s*|\Z)'
                sources_section_match = re.search(sources_section_pattern, current_note_content, re.MULTILINE | re.IGNORECASE)
                if sources_section_match:
                    sources_text = sources_section_match.group(2) # Capture content after heading
                    for line in sources_text.splitlines():
                        # Remove markdown citation format (e.g., \citep{key} or \citep[p~123]{key})
                        source_line = re.sub(r'\\citep\[?.*?\\]?{([^}]+?)}', r'\1', line).strip()
                        if source_line and not source_line.startswith('-'): # Avoid adding bullet points as sources
                            all_sources.add(source_line)
                    current_note_content = re.sub(sources_section_pattern, '', current_note_content, flags=re.MULTILINE | re.IGNORECASE)

                # 4. Extract and remove Connections/Related Concepts section
                # Match any level of heading for Connections/Related Concepts
                connections_section_pattern = r'(?s)^#+\s*Connections/Related Concepts\s*\n.*?(?=\n#+\s*|\Z)'
                current_note_content = re.sub(connections_section_pattern, '', current_note_content, flags=re.MULTILINE | re.IGNORECASE)

                # 5. Remove any internal headings from the note content itself (e.g., # Note Title, ## Subheading)
                # This prevents duplication when the script adds its own ### Note Title
                current_note_content = re.sub(r'^#+\s*.*', '', current_note_content, flags=re.MULTILINE)

                # 6. Remove any remaining WikiLinks from the content
                current_note_content = re.sub(r'\[\[([^\]]+?)\]\]', r'\1', current_note_content)

                # 7. Reduce multiple newlines to a maximum of two
                current_note_content = re.sub(r'\n\s*\n', '\n\n', current_note_content).strip()

                processed_notes_content[note_full_name] = current_note_content.strip()

            except Exception as e:
                print(f"Error reading or processing note {note_path}: {e}")
                continue

    # --- Phase 2: Generate Aggregated MOC Content ---
    final_output_lines = []
    try:
        with open(moc_file_path, 'r', encoding='utf-8') as f:
            moc_content_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: MOC file not found at {moc_file_path}")
        return
    except Exception as e:
        print(f"Error reading MOC file: {e}")
        return

    for line in moc_content_lines:
        # Find all WikiLinks in the current line
        linked_notes_in_line = re.findall(r'\[\[([^\]]+?)\]\]', line)

        # This will be the line that goes into the final output, with links replaced by titles
        current_output_line = line.rstrip()

        for linked_note_full_name in linked_notes_in_line:
            note_title_display = linked_note_full_name.split(' - ', 1)[-1].strip()

            # Replace the [[link]] with just the title in the current MOC line
            # Use re.sub with re.escape for robustness
            current_output_line = re.sub(re.escape(f'[[{linked_note_full_name}]]'), note_title_display, current_output_line)

            if note_title_display in added_note_titles_to_output:
                continue # Skip if this note's content has already been added

            if linked_note_full_name in processed_notes_content:
                note_content_to_add = processed_notes_content[linked_note_full_name]
                added_note_titles_to_output[note_title_display] = True # Mark as added

                # Add the note content as a separate block immediately after the line it was linked in
                final_output_lines.append(f"\n### {note_title_display}\n\n{note_content_to_add}\n\n---\n") # Separator between notes
            else:
                print(f"Warning: Content for linked note '{linked_note_full_name}' not found in processed notes. Skipping content insertion.")

        final_output_lines.append(current_output_line) # Append the modified MOC line

    # Add all collected sources at the end
    if all_sources:
        final_output_lines.append("\n## Collected Sources\n\n")
        for source in sorted(list(all_sources)):
            final_output_lines.append(f"- {source}\n")

    # Write to output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(final_output_lines))
        print(f"Successfully generated aggregated MOC content to {output_file_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")

# --- How to run the script ---
moc_file = "/home/qkg/PhD_Vault/MOCs/Human-in-the-loop Semi-Supervised Ensemble Learning for Fault Detection in Photovoltaic Systems - Application to a Real-World Power Plant.md"
output_file = "/home/qkg/PhD_Vault/MOC_Aggregated_Content.md"
main_notes_directory = "/home/qkg/PhD_Vault/Main_Notes/"

generate_moc_text(moc_file, output_file, main_notes_directory)