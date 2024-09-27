# Markdown Notes

### Headings

- /# is equals h1 in HTML, /## as h2 and so on till h6.
- You should put a blank line before and after a heading for compatibility

### Paragraph

Normal text just like this line are treated as paragraph tag.

### Line break

- To create a line break or new line (<br>), end a line with two or more spaces, and then type return.

### Bold and italic

- To write in bold surround text with **double Asteric** sign or __Double underscore__.
- To write in in italic surround text with *single asteric* sign or _single underscore_ .
- To write in bold and italic both combine any of above convention, you can use ***triple asteric*** you can use ___triple underscore___
- Markdown applications don’t agree on how to handle underscores in the middle of a word. For compatibility, use asterisks to italicize the middle of a word for emphasis.
  

### Blockquote

> To create a blockquote
> use > before start of the 
> line.

> Blockquote can be nested
>> just like this 
>> and this
> or can be used with other element 
> - like this

- Put blank line before and after blockquote

###  Ordered List
1. first
2. second
   - first
   - second
3. third
   1.  first
   2.  second

### Unordered List
- first
- second
  1. one 
  2. two
- third
  - ding


### Escaping Backticks
If the word or phrase you want to denote as code includes one or more backticks, you can escape it by enclosing the word or phrase in double backticks (``).

### Code block
- Surround the block with triple backtics.
```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Links
To create a link, enclose the link text in brackets (e.g., [Duck Duck Go]) and then follow it immediately with the URL in parentheses (e.g., (https://duckduckgo.com)). you can additionally ad the title. just give a space after link and enclose title with double quote.

My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").

### URLs and Email Addresses
To quickly turn a URL or email address into a link, enclose it in angle brackets.

<https://www.markdownguide.org>
<fake@example.com>

### Tables
- To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column. For compatibility, you should also add a pipe on either end of the row.
- You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row.

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |




