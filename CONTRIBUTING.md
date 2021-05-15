# How to file a bug report

If you have any suggestions for improvements please do not hesitate to
open an [issue](https://github.com/risuorg/risumetrics/issues/new).

# How to contribute code

We encourage you to contribute new plugins.  We use [gerrithub][] for
reviewing proposed changes.  The submission process looking something
like this:

[gerrithub]: https://gerrithub.io/

1. Clone the risumetrics repository:

        git clone https://github.com/risuorg/risumetrics

2. Configure the `git-review` tool:

        git-review -s

3. Check out a branch in which to make your changes:

        git checkout -b "your-new-branch"

4. Edit your files and validate with tox:

        tox # this will check the changes for some errors

    1. NOTE: tox will run python 2.7, pep8 and python 3.5 tests, if your environment lacks for example python 3.5, do execute tox -l to see the available tests and skip that one, for example:

        ~~~sh
        tox -e pep8
        tox -e py27
        # We're skipping tox -e py35 which is also invoked by default when tox is executed without arguments.
        ~~~

5. Update your local repository:

        git add $modified_files
        git commit

        For the message, please use a short line with the fix and the subject like `[plugins][openstack][nova] Check nova configuration XXX`

        If the commit fixes a github open issue, also use `Closes #$ISSUEID` so github automatically closes it once merged referencing the commit.

6. Submit your changes for review:

        git-review

Then wait for your changes to be reviewed.  It is common for reviewers
to request changes; when this happens:

1. Edit your files and revalidate with tox:

        tox # this will check the new changes for some errors

2. Update your existing commit. Do not create a new commit!

        git add $modified_files
        git commit --amend

3. Resubmit the change:

        git-review

You can see pending and already merged actual changes at: <https://review.gerrithub.io/q/risuorg>

4. Once the new plugin has been submitted you'll see some comments from 'Jenkins' which is running Unit tests against it (same ones that you run with `tox`)

5. If Jenkins gives 'Verified +1', next step is wait for one reviewer to give final ACK and merge the change.
