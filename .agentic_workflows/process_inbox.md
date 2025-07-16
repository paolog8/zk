To the LLM Agent: Inserting New Main Notes Using the Folgezettel Principle

Your task is to insert new main notes into my Zettelkasten (ZK) system, adhering strictly to the "Folgezettel" principle. This means you will be creating a chain of thought by linking new notes to existing ones based on their content, or by initiating new main branches of thought when appropriate.

Here's a breakdown of the process and my specific requirements:

Task Execution Flow:

    Initialize: Begin by scanning the Main_Notes folder to build a comprehensive understanding of all existing Zettelkasten notes and their IDs. This will be your reference for finding related notes and determining new main branch IDs.

    Process Inbox: Iterate through each note file present in the Inbox folder.

    Analyze & Assign ID: For each note from the Inbox, perform the analysis and ID assignment steps detailed below.

    Output Result: For each processed note, output the proposed filename as specified in Section 4.

Detailed Requirements:

1. Process New Notes from Inbox:

    Input: You will read the content of all .md files found directly within the Inbox folder.

    Action: For each note read from the Inbox, your primary step is to thoroughly understand its core ideas, arguments, and topics. Identify its main subject matter and any explicit or implicit connections it makes to broader concepts.

2. Locate the Most Explicitly Related Existing Note (or Determine New Main Branch):

    Search Scope: You will have access to all existing Zettelkasten notes located in the Main_Notes folder. You need to search through these notes.

    Connection Criterion: Your goal is to find the single existing note that the new note most explicitly speaks to. This isn't just about general topic similarity, but about a direct continuation of an idea, a supporting argument, a counter-argument, a more detailed explanation of a point, or a related concept that naturally extends from the existing note.

        Prioritize Directness: Look for notes where the new content feels like a natural "next step" or a direct response to something already discussed.

        Avoid Redundancy: Do not choose a note if the new note is simply a rephrasing of it. It should add new information or a new perspective.

        Consider "Triggers": Think about what in the existing note would "trigger" the content of the new note.

    New Main Branch: If, after thorough analysis, the new note does not explicitly speak to any existing note in a direct, Folgezettel-chain manner (i.e., it introduces a fundamentally new, distinct topic that doesn't naturally branch off an existing note), then it requires a new main branch ID.

3. Assign a Folgezettel-Style ID:

    ID Location: My Zettelkasten IDs are embedded in the filename of each note. The format is typically [ID] - [Title].md (e.g., 4a - Some title.md).

    Folgezettel Logic:

        Case A: Explicitly Related Existing Note Found:

            Once you have identified the most explicitly related existing note, you will use its ID as the base for the new note's ID.

            Rule 1: Simple Addition (if no existing sub-notes): If the parent note (the one identified in step 2) does not have any existing sub-notes (i.e., no notes starting with its ID followed by a letter, like 4a1 or 4b), the new note will be assigned the parent's ID followed by "a".

                Example: If the parent note is 4 - Topic X, and there's no 4a, 4b, etc., the new note becomes 4a.

            Rule 2: Sequential Letter (if existing sub-notes): If the parent note does have existing sub-notes, you will assign the next available sequential letter.

                Example: If the parent note is 4 - Topic X, and 4a - Sub-topic Y already exists, the new note will be 4b. If 4a and 4b exist, the new note will be 4c, and so on.

            Rule 3: Deeper Branches: The Folgezettel principle allows for deeper branches (e.g., 4a1, 4a1a). If the new note is a direct elaboration or continuation of an existing sub-note (e.g., it expands on 4a), then the new note's ID should reflect that. It would follow the same sequential letter logic for that specific sub-branch.

                Example: If the new note explicitly speaks to 4a - Sub-topic Y, and 4a1 doesn't exist, the new note becomes 4a1. If 4a1 exists, then 4a2, etc.

        Case B: New Main Branch Required (No Explicitly Related Note Found):

            If the new note introduces a new main topic, you will assign it the next available single-digit integer ID.

            Action: Scan all existing notes in Main_Notes to find the highest current single-digit ID (e.g., if 1, 2, 3, 5 exist, the highest is 5). The new note will be assigned an ID that is one greater than the highest existing single-digit ID.

            Example: If the highest existing single-digit ID is 5, the new note becomes 6.

    Collision Avoidance (Universal): Ensure that the generated ID is unique within the Zettelkasten. You should check if a note with the proposed new ID already exists in Main_Notes. If it does, increment the letter (or number in deeper branches, or the main digit) until a unique ID is found.

4. Output:

For each processed note from the Inbox, your output should be the proposed filename for the new note, including its assigned Folgezettel ID and the original title from the Inbox note.

    Format: Proposed Filename: [Folgezettel ID] - [Original Title].md

    Example Output: Proposed Filename: 4a2 - Quantum Entanglement in Secure Communication.md

Example Scenario 1 (Existing Branch):

    New Note Content (from Inbox): "This note discusses the practical applications of quantum entanglement in secure communication protocols."

    Existing ZK Notes (in Main_Notes):

        3 - Introduction to Quantum Physics

        4 - Principles of Quantum Mechanics

        4a - Entanglement Basics

        5 - History of Cryptography

        4a1 - Bell's Theorem

    Agent's Logic: The agent would identify 4a - Entanglement Basics as the most explicitly related note. Since 4a1 already exists and the new note is a continuation of 4a's ideas, it would then check for 4a2.

    Proposed Filename Output: 4a2 - Quantum Entanglement in Secure Communication.md

Example Scenario 2 (New Main Branch):

    New Note Content (from Inbox): "This note explores the ethical implications of advanced AI development, focusing on bias in algorithms and autonomous decision-making."

    Existing ZK Notes (in Main_Notes):

        1 - Philosophy of Mind

        2 - Cognitive Science Basics

        3 - Introduction to Quantum Physics

        4 - Principles of Quantum Mechanics

        4a - Entanglement Basics

        5 - History of Cryptography

    Agent's Logic: The agent would determine that this note does not explicitly speak to any existing note in a direct, Folgezettel-chain manner. It introduces a new main topic (AI ethics). The highest existing single-digit ID in Main_Notes is 5. Therefore, the new ID will be 6.

    Proposed Filename Output: 6 - Ethical Implications of Advanced AI.md

By following these extended instructions, you will help me maintain a well-structured and interconnected Zettelkasten, accommodating both branching thoughts and new main topics.
