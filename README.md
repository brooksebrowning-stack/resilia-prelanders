# Resilia Prelanders

Prelander pages for resilia.shop, built as Shopify theme files so they can be merged into Resilia's live theme.

## Layout

| Folder | What goes there |
|---|---|
| `sections/` | One section per prelander: `prelander-<page-id>.liquid` (markup, scoped CSS, schema) |
| `templates/` | One page template per prelander: `page.<page-id>.json` |
| `assets/` | Images and clips, prefixed with the page ID: `<page-id>-<name>.<ext>` |

## Naming

- New pages get a plain number (O1, O2). Iterations add a letter (O1a, O1b, O1c).
- Pages tied to one story ad carry the ad code: `o1a-26188` is for ad OO-26188 only and must be paired with that exact story and characters.
- Every page is also labelled in the "OOO Prelander Builds" sheet.

## Going live

1. Merge the page's branch.
2. Copy its `sections/`, `templates/` and `assets/` files into the Resilia theme (or sync this repo's files with the theme).
3. In Shopify admin, create a page and pick its template (for example `page.o1a-26188`).
4. Each section has a "Button link (product page)" setting. It defaults to the oil of oregano product page.

## Compliance

All copy follows Resilia's advertorial rules (advertorial label, FDA disclaimer, results vary, studies not conducted on Resilia products). Get sign-off before changing claims.
