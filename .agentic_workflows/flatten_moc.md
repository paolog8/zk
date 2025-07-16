To the LLM Agent: Flattening MOCs by Embedding Note Content

Your task is to flatten an existing Map of Content (MOC) by replacing all internal note links with the actual content of the linked notes. This process involves specific content filtering and aggregation.

Task Execution Flow:

    Input MOC: You will be provided with the content of a single MOC .md file. This MOC is expected to contain Obsidian WikiLinks ([[Note ID - Note Title]]) to Zettelkasten notes.

    Access Zettelkasten: You will have access to all notes in my designated Zettelkasten folder (assume this is Main_Notes).

    Process Linked Notes (Staging): For each unique note linked within the MOC, you will:

        Locate the corresponding note file in Main_Notes.

        Read its full content.

        Filter its content as per Section 3.

        Extract source information for aggregation.

        Store this processed content and source information temporarily for later insertion.

    Construct Flattened MOC: You will then iterate through the MOC content, replacing each note link with its processed content and appending the aggregated sources.

    Output Result: Your final output will be the complete, modified content of the MOC file.

Detailed Requirements:

1. Input MOC and Zettelkasten Notes:

    Input MOC: You will read the content of the MOC .md file provided.

    Zettelkasten Notes: You will read the content of all .md files found within the Main_Notes folder. These notes have filenames structured as [ID] - [Title].md (e.g., 4a - Some title.md).

2. Identify and Process Linked Notes:

    Identify Links: Scan the input MOC content to find all instances of Obsidian WikiLinks in the format [[Note ID - Note Title]].

    Retrieve Note Content: For each identified link:

        Parse the Note ID and Note Title from the link.

        Construct the expected filename: [Note ID] - [Note Title].md.

        Locate and read the content of this file from the Main_Notes folder.

3. Filter Note Content and Aggregate Sources:

For each note's content that you retrieve:

    Remove Tags: Remove all Markdown tags (e.g., #tag, #multi-word/tag, tag:value, key:: value) from the note's content.

    Discard "Connections/Related Concepts": Identify and remove any section explicitly titled "Connections", "Related Concepts", "Links", or similar, along with all its sub-content. Assume these sections are typically at the end of a note and might be denoted by a heading (e.g., ## Connections).

    Aggregate Sources:

        Identify any section explicitly titled "Source", "Sources", "References", or similar.

        Extract the content of this section.

        Do not include this source content when replacing the link in the main MOC body.

        Collect all extracted source content from all linked notes into a single, comprehensive list. This list will form a new "Sources" section at the very end of the flattened MOC. Ensure unique source entries if possible (e.g., by de-duplicating exact lines).

4. Construct the Flattened MOC:

    Replace Links: In the original MOC content, replace each [[Note ID - Note Title]] link with the processed content of the corresponding note (i.e., after tags and connection sections have been removed).

    Maintain Structure: Ensure that the original headings and overall structure of the MOC are preserved. The inserted note content should flow naturally under the heading where its link originally resided.

    Append Aggregated Sources: After all links have been replaced, append the collected and de-duplicated aggregated source content under a new, top-level heading at the very end of the MOC, titled ## Sources.

5. Output:

Your output should be the complete, modified MOC .md file content, with all links replaced by processed note content and a consolidated "Sources" section at the end.

Example Scenario:

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

Content of 4a1 - Bell's Theorem.md (from Main_Notes):

# Bell's Theorem

Bell's theorem states that no physical theory of local hidden variables can ever reproduce all the predictions of quantum mechanics.

## Related Concepts
- EPR Paradox

## Source
- Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox.

Content of 4a2 - Quantum Entanglement in Secure Communication.md (from Main_Notes):

# Quantum Entanglement in Secure Communication

Quantum Key Distribution (QKD) utilizes entanglement to ensure secure communication... #security

## Source
- Bennett, C. H., & Brassard, G. (1984). Quantum Cryptography: Public Key Distribution and Coin Tossing.

Agent's Logic:

    Reads MOC. Identifies links: [[4a - Entanglement Basics]], [[4a1 - Bell's Theorem]], [[4a2 - Quantum Entanglement in Secure Communication]].

    Retrieves content for each.

    Processes 4a - Entanglement Basics.md:

        Removes #physics #quantum.

        Removes ## Connections section.

        Extracts source: "Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information."

        Processed content: # Entanglement Basics\n\nQuantum entanglement is a phenomenon where two or more particles become linked...

    Processes 4a1 - Bell's Theorem.md:

        No tags.

        Removes ## Related Concepts section.

        Extracts source: "Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox."

        Processed content: # Bell's Theorem\n\nBell's theorem states that no physical theory of local hidden variables can ever reproduce all the predictions of quantum mechanics.

    Processes 4a2 - Quantum Entanglement in Secure Communication.md:

        Removes #security.

        No connection sections.

        Extracts source: "Bennett, C. H., & Brassard, G. (1984). Quantum Cryptography: Public Key Distribution and Coin Tossing."

        Processed content: # Quantum Entanglement in Secure Communication\n\nQuantum Key Distribution (QKD) utilizes entanglement to ensure secure communication...

    Aggregates Sources: Collects all three unique source entries.

    Replaces links in MOC and appends sources.

Expected Output (Modified MOC Content):

# Quantum Physics MOC

## Entanglement
# Entanglement Basics

Quantum entanglement is a phenomenon where two or more particles become linked...
# Bell's Theorem

Bell's theorem states that no physical theory of local hidden variables can ever reproduce all the predictions of quantum mechanics.

## Applications
### Quantum Cryptography
# Quantum Entanglement in Secure Communication

Quantum Key Distribution (QKD) utilizes entanglement to ensure secure communication...

## Sources
- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.
- Bell, J. S. (1964). On the Einstein Podolsky Rosen Paradox.
- Bennett, C. H., & Brassard, G. (1984). Quantum Cryptography: Public Key Distribution and Coin Tossing.

