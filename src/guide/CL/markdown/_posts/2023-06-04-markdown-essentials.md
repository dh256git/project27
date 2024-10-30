---
layout: post
title: Headings, lists, and links - the Markdown essentials
volume: digital skills
chapter: markdown
tag: markdown
image: /guide/robot.png
alt: A cartoon image showcases three characters personifying Markdown elements, a towering figure with oversized glasses for 'Headings', a multi-armed figure holding different items for 'Lists', and a shape-shifting figure with extending parts connecting to floating icons for 'Links'. These characters are set in a vibrant, digital workspace filled with coding symbols, highlighting the functionality and organisation of Markdown.
---

Markdown is a minimalist’s dream for creating structured, organised content without fussing over formatting. In this post, we’ll focus on three core elements—headings, lists, and links—that provide the foundation for clear, readable documents. These Markdown essentials are easy to learn, making them perfect for writers, developers, and professionals looking to streamline their workflow and make content accessible for everyone, including those using screen readers.
<!-- excerpt-end -->

### **Cheatsheet: Core Markdown Syntax**

Let’s take a quick look at some of the most commonly used Markdown syntax:

| **Markdown Element**    | **Syntax Example**               | **Result**                          |
|-------------------------|----------------------------------|-------------------------------------|
| **Header**              | `# Header 1`, `## Header 2`     | Creates headings of various sizes. |
| **Bold Text**           | `**bold text**`                 | Makes text bold.                    |
| **Italic Text**         | `*italic text*`                 | Makes text italic.                  |
| **Bullet List**         | `- Item 1`                      | Creates bulleted list items.        |
| **Link**                | `[Link Text](URL)`              | Creates a hyperlink.                |
| **Image**               | `![Alt Text](image_url)`        | Inserts an image with alt text.     |
| **Code Block**          | \```code\```                    | Displays code in a block format.    |

### **Headings: Structuring Your Content**

Headings give your document hierarchy and flow, helping readers navigate content quickly. Markdown offers six levels of headings, from the main title to sub-sections, using the `#` symbol. The more `#` symbols you use, the smaller the heading size:

```markdown
# Heading 1
## Heading 2
### Heading 3
```

The heading levels continue up to `###### Heading 6`, though most documents rarely need more than three levels for clarity.

#### **Best Practices for Headings**
1. **Start with a Single `#` for the Main Title**: Reserve `# Heading 1` for the document’s title. It’s both visually clear and accessible, helping screen readers identify the main topic.
2. **Use Lower-Level Headings for Structure**: Use `##` and `###` headings for sub-sections, keeping a logical flow that breaks down content.
3. **Accessible Navigation**: For screen reader users, heading levels create a predictable structure, making it easy to navigate through different sections with just a few keystrokes.

### **Lists: Organising Information at a Glance**

Lists are a fantastic way to make information digestible. Markdown supports two main types of lists: **unordered lists** (bullet points) and **ordered lists** (numbered lists).

#### **Unordered Lists**
Unordered lists are created using `-`, `*`, or `+` for each list item. Here’s an example:

```markdown
- First item
- Second item
- Third item
```

This will display as:
- First item
- Second item
- Third item

Unordered lists are ideal for general points, feature lists, or quick thoughts that don’t require a specific order.

#### **Ordered Lists**
Ordered lists are created by starting each line with a number, followed by a period. Markdown will automatically adjust the numbering in most editors:

```markdown
1. First item
2. Second item
3. Third item
```

Which will render as:
1. First item
2. Second item
3. Third item

**Tip:** You can number every item as “1.” and Markdown will automatically order them, making it easy to rearrange items without renumbering.

#### **Nested Lists**
Both unordered and ordered lists can be nested, making them perfect for creating detailed outlines or to-do lists. Just indent with two spaces or a tab to nest items:

```markdown
1. First item
   - Sub-item 1
   - Sub-item 2
2. Second item
```

#### **Best Practices for Lists**
1. **Keep Lists Concise**: Aim for short phrases rather than long sentences for each list item.
2. **Choose the Right Type**: Use ordered lists when sequence matters and unordered lists for everything else.
3. **Accessible Lists**: Markdown lists are straightforward for screen readers, providing a clear structure that makes scanning through items a breeze.

### **Links: Connecting Your Content**

Links are a crucial part of Markdown, allowing you to reference other documents, websites, or resources directly within your text. In Markdown, links are added by wrapping the link text in square brackets `[]` and placing the URL in parentheses `()`:

```markdown
[Project27](https://project27skills.com)
```

This will render as: [Project27](https://project27skills.com).

#### **Adding Descriptions for Accessibility**
For accessibility, it’s a best practice to write descriptive link text instead of generic phrases like “click here.” This makes it easier for screen reader users to understand the link’s purpose without needing surrounding context.

**Example:**

```markdown
[Read more about Markdown accessibility](https://example.com)
```

#### **Best Practices for Links**
1. **Use Descriptive Text**: Link text should describe the destination, aiding both readers and screen readers.
2. **Use Inline Links for Concise Content**: Inline links are compact and keep your Markdown clean.
3. **Keep URLs Short**: When possible, avoid linking lengthy URLs directly, as they can clutter the text and make it hard to read in plain-text form.

### **Markdown Essentials in Practice: A Simple Example**

Here’s how headings, lists, and links might come together in a Markdown document:

```markdown
# Markdown Essentials

## Why Use Markdown?

- Simple syntax
- Easy to read in raw form
- Great for collaboration
- Supports accessible document structure

## Useful Resources

- [Markdown Guide](https://www.markdownguide.org)
- [GitHub Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github)

## Conclusion

Markdown provides a lightweight, accessible format for creating structured documents. With just a few symbols, you can create a clean, organised document that’s readable for everyone.
```

This document would render as a well-structured piece with clear headings, lists, and links, making it easy for both visual readers and screen reader users to navigate.

### **Why Mastering These Essentials Matters**

By using headings, lists, and links effectively in Markdown, you can transform plain text into a rich, structured document that’s accessible, readable, and easy to navigate. These essentials aren’t just tools—they’re the building blocks of clear communication, making Markdown an invaluable skill for everyone from developers to content creators.

Master Markdown’s essentials, and you’ll be well on your way to writing documents that anyone can read, navigate, and enjoy!