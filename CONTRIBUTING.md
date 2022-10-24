# Contributing Guidelines

This document will contain all you need to know before you start contributing to the repository.


## 1. Ask for the issue to be assigned

If the issue has not been assigned yet, ask for it to be assigned to you. If assigned, only then start working on the issue.  
Any PRs without being assigned the issue will be closed immediately.

<br>

## 2. Forking the repository

Since you cannot directly make changes to the main repository, fork it.

<br>

## 3. Clone the forked repository

Make sure that your fork is up-to-date with the main repository and then clone it locally to start working on it using -  
``` git clone https://github.com/username/FastAPI-TODO.git```

<br>

## 4. Commit Messages

Follow the following set of commit messages while making commits to make it easier for the maitainers and other contributers to understand what changes you've made -

| Prefix | When to use? |
|--------|:-----:|
| `fix:` | Used when a small bug in the codebase is patched |
| `feat:`| Used when a new feature is added to the codebase |
| `chore:`| Used when a very minor change which can't be categorized as a new feature is done to the codebase |
| `docs:` | Used when there are changes made to the documentation and not the codebase |
| `refactor:`| Used when the codebase is refactored |
| `deps:` | Used when dependencies are added, changed or deleted |
| `style:` | Used when changes related to style are made |

The format of commit messages should be in the form -  
`<prefix>:<commit message>`

<br>

## 5. Push the changes to your fork and then create a pull request

Once you've commited the changes push them to your fork using -  

```git push```

Then check for any merge conflics, fix them and open a pull request on the main branch refrencing the issue.