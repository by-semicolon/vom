```
(parent)/
  .vom/
    README # contains info about vom for those who might not know what this directory is along with commands.
    .git/
    repo/
      contributors.ejson # contains an object of all contributors on this repository along with their first contribution, number of contributions, list of owned implementations, bio, contact and links.
      github.ejson # contains github repository url, name, author and other info.
      vom.ejson # contains useful information about vom like the current version, credits
    implementations/
      (implementation name)/
        contributors.ejson # contains an object of contributors on this implementation and their permissions and owner status.
        commits/
          (commit order number)/
            info.ejson # information on the commit like id, message, author and date/time of commit.
            (.e files with encoded file contents of all files in the commit and subdirectories of more .vom files)
```