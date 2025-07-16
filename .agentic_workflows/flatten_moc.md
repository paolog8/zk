To the LLM Agent: Flattening MOCs by Embedding Note Content (Iterative Process with Backup & Indentation Refinement)

Your task is to iteratively flatten an existing Map of Content (MOC) by replacing internal note links with the actual content of the linked notes. This process involves creating a backup, pre-processing the MOC for consistent formatting, specific content filtering, iterative replacement with proper indentation and header adjustment, and aggregated source management using a staging file.

Task Execution Flow:

    Create Backup: Make a complete backup copy of the original MOC .md file before any modifications.

    Initialize Staging: Create an empty temporary file (e.g., _moc_sources_staging.md) to collect all source entries.

    Pre-process MOC Content: Normalize the indentation and header levels of the original MOC content for consistency.

    Iterative Link Replacement:

        Work with the pre-processed MOC content. This will be your current MOC content.

        Repeatedly find and process the next [[Note ID - Note Title]] link within the current MOC content.

        For each found link:

            Determine its indentation level and the effective heading level of the section it's in.

            Locate and read the content of the corresponding note from the Main_Notes folder on demand.

            Filter this note's content (remove tags, discard connection sections).

            Extract source information from this note and append it to the _moc_sources_staging.md file.

            Determine if a header citation is needed based on the note's body content.

            Adjust the note's internal headings relative to the MOC's structure.

            Replace only that one link in the current MOC content with the note's original title (including its ID) as a heading, potentially with a citation, followed by its processed content, all with appropriate indentation.

            Update the current MOC content with this single replacement.

        Continue this step until no more links are found in the current MOC content.

    Finalize Sources:

        Read all content from _moc_sources_staging.md.

        De-duplicate the source entries.

        Append this de-duplicated, aggregated source content under a new ## Sources heading at the very end of the current MOC content.

    Output Result: Your final output will be the complete, modified content of the MOC file.

Detailed Requirements:

1. Input MOC and Zettelkasten Notes:

    Input MOC: You will read the content of the MOC .md file provided.

    Zettelkasten Notes: You will read the content of all .md files found within the Main_Notes folder. These notes have filenames structured as [ID] - [Title].md (e.g., 4a - Some title.md).

2. Create MOC Backup:

    Before any processing begins, create a copy of the input MOC file.

    Backup Filename: Append .bak to the original filename (e.g., My MOC.md becomes My MOC.md.bak). If a .bak file already exists, you can overwrite it or append a timestamp (e.g., My MOC.md.bak_YYYYMMDD_HHMMSS).

3. Pre-process Original MOC Content for Consistency:

    Before starting link replacement, analyze the entire input MOC content.

    Normalize Indentation: Ensure consistent indentation for list items. For nested lists, each level should be indented by 2 spaces relative to its parent. Correct any inconsistent leading whitespace.

    Normalize Headers (if necessary): While MOCs generally have consistent headers, ensure they follow a logical hierarchy (e.g., ## for main sections, ### for subsections). If any obvious structural issues are present (e.g., a #### directly under a #), attempt to normalize them to maintain a clear hierarchy.

4. Iterative Construction of the Flattened MOC:

    Start with a variable holding the current MOC content, initialized with the pre-processed original MOC content.

    Loop: While the current MOC content still contains [[Note ID - Note Title]] links:

        Find the first occurrence of a [[Note ID - Note Title]] link in the current MOC content.

        Determine Contextual Indentation and Heading Level:

            Identify the leading whitespace (indentation) of the line containing the found link. This indentation should be preserved for the inserted content.

            Determine the Markdown heading level of the closest preceding heading in the current MOC content. This is the "current effective heading level."

        On-Demand Note Processing:

            Parse the Note ID and Note Title from this specific link.

            Construct the expected filename: [Note ID] - [Note Title].md.

            Locate and read the content of this file from the Main_Notes folder.

            Filter Content:

                4.1 Remove Tags: Remove all Markdown tags (e.g., #tag, #multi-word/tag, tag:value, key:: value) from the note's content.

                4.2 Discard "Connections/Related Concepts": Identify and remove any section explicitly titled "Connections", "Related Concepts", "Links", or similar, along with all its sub-content. Assume these sections are typically at the end of a note and might be denoted by a heading (e.g., ## Connections).

            4.3 Extract and Stage Sources (to File): Identify any section explicitly titled "Source", "Sources", "References", or similar. Extract the content of this source section and append it to the _moc_sources_staging.md file. Ensure each source entry is on a new line.

            4.4 Determine Header Citation:

                Analyze the body of the note (after tags and connection sections are removed) for explicit in-text citations. Look for common patterns like \citep{...}, \cite{...}, (Author, Year), [Number], etc.

                If no explicit in-text citations are found in the note's body:

                    From the source section of the current note being processed (before it's appended to _moc_sources_staging.md), identify the first source entry.

                    Extract the primary author/organization and year from this first source entry.

                    Format this as ([Author/Org] Year).

                If explicit in-text citations are found, no citation is added to the header.

        Prepare Inserted Content:

            Take the processed content of the note.

            Adjust Internal Headings: For every heading (#, ##, ###, etc.) within the note's processed content, increase its level by one hash (#) relative to the current effective heading level of the MOC section. For example, if the MOC section is ##, and the note starts with #, it becomes ###. If the note starts with ##, it becomes ####, and so on. Ensure no heading exceeds ######.

            Apply Indentation: Apply the leading whitespace of the original link's line to every line of the adjusted note content, including its new title heading. If the link was part of a list item (e.g., - [[...]]), ensure the inserted content maintains that list item's indentation.

        Replace Link: Replace only this single instance of the link in the current MOC content with the following structure, ensuring correct indentation:

        [Original Link's Indentation]### [Note ID] - [Original Note Title] [Optional Citation]
        [Original Link's Indentation]
        [Original Link's Indentation][Processed Note Content, with adjusted internal headings and consistent indentation]

        Where [Optional Citation] is the ([Author/Org] Year) determined in step 4.4, or empty if explicit citations were found in the body.
        (The ### for the inserted note title is a base suggestion; the agent should determine the appropriate heading level based on the current MOC context and the note's original top-level heading.)

        Update the current MOC content variable with the result of this replacement.

    Maintain Structure: Ensure that the original MOC headings and overall structure are preserved. The inserted note content should flow naturally under the heading where its link originally resided.

5. Finalize and Append Aggregated Sources:

    Read the entire content of the _moc_sources_staging.md file.

    De-duplicate the source entries from the collected content.

    Append this de-duplicated, aggregated source content under a new, top-level heading at the very end of the current MOC content, titled ## Sources.

6. Output:

Your output should be the complete, modified MOC .md file content (the final current MOC content variable), with all links replaced by processed note content and a consolidated "Sources" section at the end.

Staging File Details:

    _moc_sources_staging.md: This temporary file will be used to accumulate all source entries extracted from individual notes. It is built iteratively as links are processed. It should be created at the beginning of the process and can be deleted or cleared after the final MOC output is generated. Its purpose is to allow for efficient de-duplication of sources at the very end.

Example Scenario (Illustrating Indentation and Header Adjustment):

MOC File Content (Provided as Input):

# Quantum Physics MOC

## Entanglement
- [[4a - Entanglement Basics]]
  - More details: [[4a1 - Bell's Theorem]]

## Applications
### Quantum Cryptography
- [[4a2 - Quantum Entanglement in Secure Communication]]

Content of 4a - Entanglement Basics.md (from Main_Notes):

# Entanglement Basics

Quantum entanglement is a phenomenon where two or more particles become linked...

## Key Properties
- Non-local correlation
- Instantaneous collapse

## Source
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.

Agent's Logic (Illustrative Iteration for 4a - Entanglement Basics):

    ... (Backup & Staging Init) ...

    Pre-process MOC: (Ensures -  and  - are consistent).

    Iterative Link Replacement:

        Initial current MOC content: (as above)

        Iteration 1: Finds [[4a - Entanglement Basics]].

            Context: Link is on a line starting with -  (2 spaces indentation for content). Closest preceding heading is ## Entanglement.

            Reads 4a - Entanglement Basics.md.

            Processes content (removes tags, connections).

            Extracts source, appends to _moc_sources_staging.md.

            Determines header citation (none needed for this example, assuming in-text citations exist or it's not a full note citation case).

            Prepare Inserted Content:

                Original note's top heading: # Entanglement Basics

                MOC's effective heading level: ## (level 2)

                Adjusted heading for insertion: ### Entanglement Basics (level 3, 2+1=3)

                Apply indentation: Every line of processed content will start with -  (original bullet indentation).

            Replaces the link.

            current MOC content becomes:

            # Quantum Physics MOC

            ## Entanglement
            - ### 4a - Entanglement Basics

              Quantum entanglement is a phenomenon where two or more particles become linked...

              #### Key Properties
              - Non-local correlation
              - Instantaneous collapse
            -   - More details: [[4a1 - Bell's Theorem]]

            ## Applications
            ### Quantum Cryptography
            - [[4a2 - Quantum Entanglement in Secure Communication]]

            (Note: The   - More details: line's indentation should be preserved from the original MOC structure by the agent, showing the nested list.)

Expected Output (Illustrative snippet for 4a - Entanglement Basics):

# Quantum Physics MOC

## Entanglement
- ### 4a - Entanglement Basics

  Quantum entanglement is a phenomenon where two or more particles become linked...

  #### Key Properties
  - Non-local correlation
  - Instantaneous collapse
-   - More details: [[4a1 - Bell's Theorem]]

... (rest of MOC) ...


