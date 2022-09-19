This directory collects "newsfragments": short files that each contain
a snippet of ReST-formatted text that will be added to the next
release notes. This should be a description of aspects of the change
(if any) that are relevant to users. (This contrasts with the
commit message and PR description, which are a description of the change as
relevant to people working on the code itself.)

Each file should be named like `<ISSUE>.<TYPE>.rst`, where
`<ISSUE>` is an issue numbers, and `<TYPE>` is one of:

* `feature`
* `bugfix`
* `performance`
* `doc`
* `internal`
* `removal`
* `misc`
* `breaking`

So for example: `123.feature.rst`, `456.bugfix.rst`

If the PR fixes an issue, use that number here. If there is no issue,
then open up the PR first and use the PR number for the newsfragment.

Note that the `towncrier` tool will automatically
reflow your text, so don't try to do any fancy formatting. Run
 `towncrier build --draft` to get a preview of what the release notes entry
 will look like in the final release notes.
