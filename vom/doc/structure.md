```
(parent)/
  .vom/
    README # contains info about vom for those who might not know what this directory is along with commands.
    .git/
    info/
      contributors.ejson # contains an object of all contributors on this repository along with their first contribution, number of contributions, list of owned implementations, bio, contact and links.
      github.ejson # contains github repository url, name, author and other info.
      vom.ejson # contains useful information about vom like the current version, credits
      rules.ejson # global rules
    implementations/
      (implementation name)/
        info/
          owners.ejson # list of usernames of the owners of the implementation
          contributors.ejson # contains an array of contributors on this implementation
          rules.ejson # rules for this implementation, overrides global rules
        commits/
          (commit number)/
            ID.etxt # file with the commit id.
            MSG.etxt # file with the provided commit message.
            (.e files with encoded file contents of all files in the commit and subdirectories of more .vom files)
        track/
          (.e files with encoded file contents of all tracked files in the implementation and subdirectories of more .vom files)
```