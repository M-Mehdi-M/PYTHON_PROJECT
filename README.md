# Student Management System

The application implements a menu-driven student management system in Python that stores student records in a flat text file (`database.txt`), with each record holding a student's name, ID number, and a growing list of enrolled classes with their credit value and score.

## Data format

Each line in `database.txt` represents one student:
`Student name == <name>,Student id number == <id>,<class>==> Credit==<credit> Score==<score>, ...`

New students start with just a name and ID; classes are appended to the line as they're registered.

## Main menu

The program runs in a loop presenting six options: Create, Update, Delete, Reports, Archive file, and Exit.

## Create

- Prompts for a student name and a 6-digit ID number, re-prompting until the ID length is valid.
- `searcher` checks whether the ID already exists in `database.txt`; if not, it appends a new line with the student's name and ID.

## Update

A submenu with two actions:

- **Enter new score** (`searcher1`) — looks up the student by ID, checks whether the class is already registered, sums the student's currently registered credits, and blocks registration if adding the new class would push total credits over 18. If everything checks out, it inserts the new class (with its credit and score) into the student's line.
- **Modify existing score** (`searcher2`) — looks up the student and class, replaces the existing score substring for that class with the new score, and rewrites the file.

## Delete

A submenu with two actions:

- **Remove Student** (`searcher3`) — finds the student's line by ID and removes it entirely from the file.
- **Remove Class** (`searcher4`) — finds the student's line, removes the matching class entry, and rejoins the remaining fields, handling the different cases of removing the last class in the line versus a middle one (with or without a trailing newline).

## Reports

A submenu with four reports, all computed by parsing `database.txt` on demand:

- **Alphabetical order** — extracts every student's name and sorts the list.
- **Academic probation** — computes each student's credit-weighted average score and lists students whose average is below 12; students with no classes are reported separately instead of being scored.
- **Sorted by average score** — computes each student's average score and prints all student names ordered from highest to lowest average.
- **Detailed performance report** — for a given student ID, prints their full record line and credit-weighted average, then recomputes an (unweighted) average-score ranking across all students to report that student's placement in the class.

## Archive file

A submenu to inspect or clear the underlying data file:

- **View Archive File Contents** — prints the raw contents of `database.txt`.
- **Delete Archive File** — overwrites `database.txt` with an empty string, erasing all records.

## Exit

Selecting Exit prints a closing message and ends the program loop.
