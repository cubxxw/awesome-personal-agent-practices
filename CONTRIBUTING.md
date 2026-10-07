# Contributing

Suggest one useful resource at a time through an issue or pull request. English and Chinese suggestions are welcome.

A good entry has a public, canonical link; a clear connection to personal agents; and a short explanation of what a reader will learn. Products should link to their official site, projects to the maintained repository, and cases to the original author's post.

For a use case, say what the person did, which tools or setup it required, and what they still handled themselves. Separate an author's report from a reproduced result. Templates, demos and synthetic examples are welcome when labeled clearly.

Keep relevant limitations and author affiliations. Do not submit private conversations, credentials, signed sharing links, copied articles or unsupported savings claims. A popular post can be a discovery lead without being a reliable implementation guide.

## Updating the catalog

1. Edit `data/catalog.json`. Each resource has a stable ID, section, category, English and Chinese annotations, source links, reading scope and the actual review date.
2. Preserve the distinction between `official`, `official-partial`, `open-source`, `reported`, `implementation-account`, `research` and `collection` evidence.
3. Run `python3 scripts/catalog.py` to regenerate both languages.
4. Run `python3 scripts/catalog.py --check` before submitting.

The root `checked_on` is the collection's editing date; each resource's `checked_on` is its own content-review date. Advance them only when the corresponding work was done. Regeneration alone is not a new source review.

Generated READMEs should be changed through the catalog or renderer. Keep introductions and annotations brief. Every resource appears directly in each README; only detailed reading scope belongs in collapsible source notes. Do not introduce separate category reading pages.

Original annotations and utility code are dedicated under CC0. Linked works keep their original licenses and rights.
