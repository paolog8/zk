# Flatten MOC workflow
--Start of workflow--
To the LLM Agent: Flattening MOCs by Embedding Note Content (Iterative Process with Backup)

Your task is to iteratively flatten an existing Map of Content (MOC) by replacing internal note links with the actual content of the linked notes. This process involves creating a backup, specific content filtering, iterative replacement, and aggregated source management using a staging file.

Task Execution Flow:

    Create Backup: Make a complete backup copy of the original MOC .md file before any modifications.

    Initialize Staging: Create an empty temporary file (e.g., _moc_sources_staging.md) to collect all source entries.

    Iterative Link Replacement:

        Read the content of the target MOC .md file. This will be your current MOC content.

        Repeatedly find and process the next [[Note ID - Note Title]] link within the current MOC content.

        For each found link:

            Locate and read the content of the corresponding note from the Main_Notes folder on demand.

            Filter this note's content (remove tags, discard connection sections).

            Extract source information from this note and append it to the _moc_sources_staging.md file.

            Determine if a header citation is needed based on the note's body content.

            Replace only that one link in the current MOC content with the note's original title (including its ID) as a heading, potentially with the required citations , followed by its processed content.

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

3. Iterative Construction of the Flattened MOC:

    Start with a variable holding the current MOC content, initialized with the original input MOC content.

    Loop: While the current MOC content still contains [[Note ID - Note Title]] links:

        Find the first occurrence of a [[Note ID - Note Title]] link in the current MOC content.

        On-Demand Note Processing:

            Parse the Note ID and Note Title from this specific link.

            Construct the expected filename: [Note ID] - [Note Title].md.

            Locate and read the content of this file from the Main_Notes folder.

            Filter Content:

                3.1 Remove Tags: Remove all Markdown tags (e.g., #tag, #multi-word/tag, tag:value, key:: value) from the note's content.

                3.2 Discard "Connections/Related Concepts": Identify and remove any section explicitly titled "Connections", "Related Concepts", "Links", or similar, along with all its sub-content. Assume these sections are typically at the end of a note and might be denoted by a heading (e.g., ## Connections).

            3.3 Extract and Stage Sources (to File): Identify any section explicitly titled "Source", "Sources", "References", or similar. Extract the content of this source section and append it to the _moc_sources_staging.md file. Ensure each source entry is on a new line.

            3.4 Determine Header Citation:

                Analyze the body of the note (after tags and connection sections are removed) for explicit in-text citations. Look for common patterns like \citep{...}, \cite{...}, (Author, Year), [Number], etc.

                If no explicit in-text citations are found in the note's body:

                    From the source section of the current note being processed (before it's appended to _moc_sources_staging.md), identify all source entries.

                    For each source entry, extract the primary author/organization and year.

                    Format these as a comma-separated list of ([Author/Org] Year) pairs.

                        Example: For sources "IEA, "Renewables 2024..." \citep{ieaRenewables20242024}" and "Smith, J. (2023). Another Study.", extract "IEA 2024" and "Smith 2023" to form "(IEA 2024, Smith 2023)".

                    This formatted string will be included in the header.

                If explicit in-text citations are found, no citation is added to the header.

        Replace Link: Replace only this single instance of the link in the current MOC content with the following structure:

        ### [Note ID] - [Original Note Title] [Optional Citation]

        [Processed Note Content]


        Where [Optional Citation] is the ([Author/Org] Year) determined in step 3.4, or empty if explicit citations were found in the body.
        (Use ### for the inserted note title to maintain hierarchy, or ## if it's a top-level note in the MOC and the MOC's main headings are ##).

            Indentation: Ensure that the ### [Note ID] - [Original Note Title] [Optional Citation] heading and every line of the [Processed Note Content] are indented to match the indentation level of the original [[Note ID - Note Title]] link they are replacing. For example, if the link was preceded by -  or    -, apply that same leading whitespace to the inserted content.

        Update the current MOC content variable with the result of this replacement.

    Maintain Structure: Ensure that the original MOC headings and overall structure are preserved. The inserted note content should flow naturally under the heading where its link originally resided.

4. Finalize and Append Aggregated Sources:

    Read the entire content of the _moc_sources_staging.md file.

    De-duplicate the source entries from the collected content.

    Append this de-duplicated, aggregated source content under a new, top-level heading at the very end of the current MOC content, titled ## Sources.

5. Output:

Your output should be the complete, modified MOC .md file content (the final current MOC content variable), with all links replaced by processed note content and a consolidated "Sources" section at the end.

Staging File Details:

    _moc_sources_staging.md: This temporary file will be used to accumulate all source entries extracted from individual notes. It is built iteratively as links are processed. It should be created at the beginning of the process and can be deleted or cleared after the final MOC output is generated. Its purpose is to allow for efficient de-duplication of sources at the very end.

Example Scenario (Illustrating Iteration and Retained Titles with Citation):

MOC File Content (Provided as Input):

# Quantum Physics MOC

## Entanglement
- [[4a - Entanglement Basics]]
- [[4a1 - Bell's Theorem]]

## Applications
### Quantum Cryptography
- [[4a2 - Quantum Entanglement in Secure Communication]]


Content of 4a - Entanglement Basics.md (from Main_Notes):

# Entanglement Basics

Quantum entanglement is a phenomenon where two or more particles become linked... #physics #quantum

## Connections
- [[4b - Superposition Explained]]

## Source
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.


Content of 4 - Solar PV Dominates Global Renewable Capacity Growth.md (example for new citation rule):

# 4 - Solar PV Dominates Global Renewable Capacity Growth
New solar capacity is projected to account for 80% of the growth in global renewable power between 2024 and 2030.
This rapid growth is attributed to declining costs, shorter permitting timelines, and widespread social acceptance.

See also: [[4a - China dominates solar and wind deployment]]

## Sources
- IEA, "Renewables 2024: Analysis and forecast to 2030" \citep{ieaRenewables20242024}
- World Energy Council. (2023). Global Energy Report 2023.


Agent's Logic (Illustrative Iteration for a note like the PV example):

    Create Backup: Quantum Physics MOC.md is copied to Quantum Physics MOC.md.bak.

    Initialize: Create _moc_sources_staging.md.

    Iterative Link Replacement:

        ... (previous iterations for Quantum Physics MOC) ...

        Assume MOC now contains [[4 - Solar PV Dominates Global Renewable Capacity Growth]]

        Iteration N: Finds [[4 - Solar PV Dominates Global Renewable Capacity Growth]].

            Reads 4 - Solar PV Dominates Global Renewable Capacity Growth.md.

            Processes its content (removes tags, connections, "See also" line).

            Determines Header Citation (Step 3.4):

                Analyzes the processed body: "New solar capacity is projected to account for 80% of the growth in global renewable power between 2024 and 2030. This rapid growth is attributed to declining costs, shorter permitting timelines, and widespread social acceptance."

                Detects no explicit in-text citations.

                Identifies all sources:

                    "IEA, "Renewables 2024: Analysis and forecast to 2030" \citep{ieaRenewables20242024}"

                    "World Energy Council. (2023). Global Energy Report 2023."

                Extracts "IEA" and "2024" from the first, "World Energy Council" and "2023" from the second. Forms "(IEA 2024, World Energy Council 2023)". This will be included in the header.

            Extracts sources, appends to _moc_sources_staging.md.

            Replaces the link.

            current MOC content now includes (assuming original link was at  - [[...]]):

            - ### 4 - Solar PV Dominates Global Renewable Capacity Growth (IEA 2024, World Energy Council 2023)
            -
              New solar capacity is projected to account for 80% of the growth in global renewable power between 2024 and 2030.
              This rapid growth is attributed to declining costs, shorter permitting timelines, and widespread social acceptance.


        Loop Ends: No more links found.

    Finalize Sources:

        Reads _moc_sources_staging.md.

        De-duplicates sources.

        Append to current MOC content.

Expected Output (Illustrative snippet for the PV note):

...
- ### 4 - Solar PV Dominates Global Renewable Capacity Growth (IEA 2024, World Energy Council 2023)
-
  New solar capacity is projected to account for 80% of the growth in global renewable power between 2024 and 2030.
  This rapid growth is attributed to declining costs, shorter permitting timelines, and widespread social acceptance.
...
## Sources
- IEA, "Renewables 2024: Analysis and forecast to 2030" \citep{ieaRenewables20242024}
- World Energy Council. (2023). Global Energy Report 2023.
...

--End of workflow--

