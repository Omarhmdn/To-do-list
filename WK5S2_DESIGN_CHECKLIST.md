# To-Do List Application - Design Document

**Team Name**: V.O.L.T

**Team Members**: Omar Hamdan, Lucas Clowe :) , Vishnu Pandaraparambath, Taiyler Popat

**Date**: 30/10/2025

---

## 1. Requirements Analysis

### 1.1 Research Notes
After exploring existing to-do list applications (Microsoft To-Do, Trello, GitHub Projects, etc.), we observed the following common features:

**What can these applications do?**
- Add Task
- Remove Task
- Mark/Unmark as completed
- Display List
- Sort

**What data do they store?**
- Tasks
- State (completed/uncompleted)
- Deadline/date

**How do they display data?**
- Sorted by Input (Stack)
- Sorted by completion (Stack)
- Sorted by Deadline/due date

---

### 1.2 Essential Features
List the features your to-do list MUST have to be functional:

1. Display
2. Add task
3. Remove Task

**Why are these essential?**
They are the important and basic functions of a to-do list, allowing a user to add, remove, display, mark state of completion
--- 

### 1.3 Desirable Features
List nice-to-have features that would enhance the application but aren't strictly necessary:

1. Sorting function
2. Editting an existing task
3. Completed/uncompleted
4. Reminder (using emails)
5. Log in Feature/multiple uses
6. Undo-Redo
---

## 2. Data Structure Design

A dictionary to store the categories where the key is the category (name of to-do list(s)) and value is a list of lists to allow mutability.

The list is to store the values of the to-do list along with Boolean to check if its done or not, along with the date and time.

Stack to undo and redo choices.

### 2.1 Task Data
What information does each individual task need to store?

| Data Field | Data Type | Purpose | Example |
|------------|-----------|---------|---------|
| | | | |
| | | | |
| | | | |

---

### 2.2 Task List Structure
How will you store the collection of tasks?

**Chosen Structure** (e.g., list of dictionaries, list of lists, list of tuples):


**Why did you choose this structure?**


**Example of your data structure with 2-3 sample tasks**:
```python
# Write your example here




```

**How will you access specific fields?** (e.g., for list of dicts: `task["description"]`)


---

## 3. Input/Output Design

### 3.1 Keyboard Input
What inputs will need to be provided?

| Input Type | When Required | Validation Needed |
|------------|---------------|-------------------|
| | | |
| | | |

---

### 3.2 Screen Output
How will you display information?

**Menu Design**:
```
[Sketch your main menu here]




```

**Task Display Format**:
```
[Show how you'll display a list of tasks]




```

---

### 3.3 File I/O
How will you handle file operations?

**File format** (CSV, JSON, plain text, etc.):

**Why this format?**


**Example of file structure**:
```
[Show what your saved file will look like]




```

**When will you load data?**


**When will you save data?**


---

## 4. Program Flow

### 4.1 Main Loop Structure
Describe or draw a flowchart of how your program will run:

```
[Pseudocode or description of main loop]
1.
2.
3.
4.
```

---

### 4.2 Error Handling
What could go wrong, and how will you handle it?

| Potential Error | How to Handle |
|----------------|---------------|
| File doesn't exist | |
| Invalid user input | |
| Empty task list | |
| | |

---

## 5. Function Specifications

For each function your team will implement, specify:
- Function name
- Purpose
- Parameters (with types)
- Return value (with type)
- Brief description of what it does

### Example:
```python
def add_task(task_list, description, priority):
    '''
    Add a new task to the task list.

    Parameters:
        task_list (list): The list of all tasks
        description (str): The task description
        priority (str): Priority level ('high', 'medium', 'low')

    Returns:
        list: Updated task list with the new task added
    '''
    pass
```

### Your Functions:

**Function 1:**
```python




```

**Function 2:**
```python




```

**Function 3:**
```python




```

**Function 4:**
```python




```

**Function 5:**
```python




```

**Function 6:**
```python




```

*(Add/ remove functions as needed)*

---

## 6. Peer Feedback Record

### Feedback Received (from other team):
**Date**: _________  **Reviewing Team**: _________________

**Strengths of our design**:
-
-

**Suggestions for improvement**:
-
-

**Changes we made after feedback**:
-
-

---

### Feedback Given (to other team):
**Date**: _________  **Team Reviewed**: _________________

**What we liked**:
-
-

**Constructive suggestions**:
-
-

---

## 7. Design Decisions Log

As you work through the design, record important decisions and why you made them:

| Decision | Options Considered | Final Choice | Reasoning |
|----------|-------------------|--------------|-----------|
| | | | |
| | | | |
| | | | |

---

## 8. Next Steps

Before starting implementation, make sure:

- [ ] All team members understand the data structure
- [ ] All function signatures are agreed upon
- [ ] Everyone knows which functions they will implement
- [ ] Git repository is set up and all members have access
- [ ] Branch naming strategy is agreed
- [ ] Testing approach is discussed (Next week's class will cover this)

**Ready to code?** Make sure all boxes are ticked!
