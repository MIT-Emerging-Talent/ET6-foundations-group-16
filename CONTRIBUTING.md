# How to Contribute

Thank you for contributing to **ET6-foundations-group-16**! 🎉 We are excited to
have you on board. This document will guide you through the process of
contributing to the project. Please read through the steps carefully to help us
maintain high-quality code and collaboration. 👩‍💻👨‍💻

## Introduction

This project aims to **improve the quality of software development through peer
code reviews** 📝🔍. We welcome contributions that enhance the code review
process, ensure coding best practices, and help maintain a clean, efficient, and
well-documented codebase. 📚✅ By participating, you help us build a better
repository where developers can share feedback and improve their coding skills
collaboratively. 🤝💡

We believe that a strong code review process is crucial to writing clean,
maintainable code and fostering a collaborative development environment. 💪
Your contribution in enhancing this process, whether through tools,
documentation, or improved review guidelines, is highly valued. 🌟  

## Contribution Guidelines ✨

Before you begin contributing, please review these guidelines to help us
maintain a consistent and high-quality codebase:

- **Fork the Repository** 🍴: Always fork the repository before making changes.
  This ensures that you have a personal copy of the code to work on.
- **Work in Small, Focused Branches** 🌱: Create a new branch for each feature,
  bug fix, or improvement. Name your branch descriptively based on what you're
  working on.
- **Write Clear Commit Messages** ✏️: Make your commit messages concise and
  descriptive. For example, instead of "Fix bug", use "Fix issue with divide by
  zero."
- **Test Your Code** 🧪: Ensure that your code is tested and works as expected.
  If you're adding features, write appropriate tests to verify functionality.
- **Keep Pull Requests Small** 🚀: Focus on one task per pull request. This
  makes it easier to review and reduces the likelihood of conflicts.
- **Respect the Code of Conduct** 🤝: Follow our community's code of conduct
  and behave respectfully in all interactions.

We are committed to maintaining a collaborative and inclusive environment,
and your contribution will play a vital role in the project's success. 🌍💼
With that in mind, let's dive into the steps for contributing! 🏁

---

## Guide to Contributing to the Repository 📚

<!--##### @Faisal Minawi:   -->
<!--Add your part   -->
<!--Add your part   -->
<!-- Add Break line or Boundary at
 the End of your part to keep it nice and organized  -->
<!--#### @Majd ABUALSOUD:   -->
<!--Add your part   -->
<!--Add your part   -->
<!-- Add Break line or Boundary at
 the End of your part to keep it nice and organized  -->
## Best Practices for Collaboration 🤝

Collaboration is key to successful teamwork, and following best practice helps
heep everything running smoothly. Below are some important practices to follow,
complete with examples to ensure effective collaboration:

### Write Commit Messages 📝

Commit messages should clearly describe what changes
have been made and why. A well-written commit message helps other developers
understand the purpose of the change and make it easier to navigate
the project's history.

   **Best Practice for Commit Messages:** ✏️

- **Be clear and concise:** Briefly describe what was changed and why.
- **Follow a consistent format:** This makes it easier to read and understand.
- **Use the imperative mood:** Write messages as commands (e.g "Fix bug"
 instead of "Fixed bug").

 **Examples:**

- **Good Commit Message:**

```bash
  git commit -m "Fix bug in user login validation"
```

  **Explanation:** This message clearly explains that a bug in the
validation has been fixed, which helps others understand the purpose of the change.

- **Bad Commit Message:**

```bash
git commit -m "Fixed login"
```

  **Explanation:** This message is vague and doesn't explain what part of the
login process was fixed or why.
  **Why this important:** Clear commit messages make it easier for your team to
understand changes without needing to dive into the code, and they make reviewing
and tracking changes much easier.

---

### Use Proper Branching Strategies 🌱

Use a structured branching strategy ensures the team works in an organized manner.
Each new task should be worked on in its won branch, which keeps the main
codebase clean and makes collaboration easier.
**Best Practices for Branching:**

- **Create a branch for each task:** Each feature, bug fix, or improvement
should have its own branch.

- **Name branches descriptively:** Use branch names that reflect the task you're
working on.

**Examples:**

- **Feature Branch:**

```bash
git checkout -b feature/login-page
```

**Explanation:** You're creating a branch specifically to work on the login
page feature

- **Bug Fixe Branch:**

```bash
git checkout -b bugfix/fic-header-alignment
```

**Explanation:** This branch is dedicated to fixing an issue with the header alignment.

- **Hotfix Branch:**

```bash
git checkout -b hotfix/fix-crash-on-startup
```

**Explanation:** A hotfix branch is used to add a critical issue, such as a
when starting the application.

**Why this is important:** By creating separate branches for each task and naming
them descriptively, the team can work on multiple tasks at once without interfering
with each other's work. It also makes it easy to track what each branch is
working on.

---

## **Resolving Merge Conflicts 🔧**

Merge conflicts occur when two or more team members changes to the same part of
a file. You need to resolve these conflicts manually to make sure that all
changes are merged correctly.

**Steps for Resolving Merge Conflicts:**

 **Understanding Merge Conflicts** When there's a conflict,
Git will mark the conflicting areas in the file. These markers indicate the
changes made by both you and the other developer.

Imagine two developers are working on the Markdown file ```README.md``` or
python file ```Calculation.py```  for example, in Markdown file:

```Markdown
<<<<<<< HEAD
# How to Contribute  
This guide will help you contributing effectively.

=======
# How to Contribute 

This document explains the best practices for contributing to the project.
>>>>>>> fearuer/section-1
```

In this case, the conflict is in the header(```# How to contribute```), and
both versions contain different text following the heading.

Similarly, in a **Python file**, a conflict could look like this:

```python
<<<<<<< HEAD
def greeting():
    print("Welcome to the project!")
=======
def greeting():
    print("Hello, thanks for contributing!") 
>>>>>>> fearuer/greeting
```

### **How to Resolve Merge Conflicts** 🔧

  **Steps for resolving conflicts in Markdown or Python files:**

- **Step 1: Identify the Conflict** 🕵️‍♂️
- Look for the conflict markers. You will see:
  - ```<<<<<<< HEAD```: The changes you made.
  - ```=======```: The division between your changes and the incoming changes.

  - ```>>>>>>> branch-name```: the changes made by someone else (in the
specified branch)

**Example (Markdown conflict):**

```markdown

<<<<<<< HEAD

# How to Contribute

This guide will help you contribute effectively
=======

# How to Contribute

This document explains the best practices for contributing to the project.
>>>>>>> feature/section-1

```

- **Step 2: Decide which changes to keep** ⚖️

  - You need to decide if you want to keep your changes, the other person’s
changes, or merge both sets of changes.

**In the Markdown file**, you might want to combine both sentences:

```markdown
# How to Contribute

This guide will help you contribute effectively and explains the best practices
for contributing to the project.
```
<!-- I break the rule to show an example-->

**In the Python file,** you could keep both greetings or choose one:

```python
def greeting():
    print("Welcome to the project!")
    # Or, combine both greetings:
    # print("Hello, thanks for contributing!")
```

- **Step 3: Remove Conflict Markers** 🧹

  - **After deciding, delete the conflict marker(```<<<<<<```,
```======```, and ```>>>>>>```). For instance, in Markdown:**

```markdown

# How to Contribute

This guide will help you contribute effectively and explains the best practices
for contributing to the project.
```
<!-- I break the rule to show an example -->
---
By following these steps, you'll resolve conflicts easily, whether you'er working
on a **Markdown** file or a **Python file**. The key is to understand the
changes, merge them carefully, and test everything before committing your changes.

We are excited to have your contribution to improve the repository and help us
build better software together! 💪
