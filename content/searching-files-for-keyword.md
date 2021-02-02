---
Title: Searching Files for Keyword in Terminal
Date: 2020-09-13
Tags: Terminal
Author: Joe
Keywords: ubuntu 20.4,
---


This is a simple post to document a recent learning. I realized my blog had multiple authors listed due to me being inconsistent with how I wrote it. Sometimes I used "Joe" or other times "Joe Lotz". I *googled* and found a terminal command to search a directory for keywords.

```bash
find /DIR_TO_SEARCH/ -type  f -exec grep --color -HIi 'KEYWORD_OR_PHRASE' {} +
```

