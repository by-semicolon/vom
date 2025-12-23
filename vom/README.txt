vvvvvvv           vvvvvvv ooooooooooo      mmmmmmm    mmmmmmm   
 v:::::v         v:::::voo:::::::::::oo  mm:::::::m  m:::::::mm 
  v:::::v       v:::::vo:::::::::::::::om::::::::::mm::::::::::m
   v:::::v     v:::::v o:::::ooooo:::::om::::::::::::::::::::::m
    v:::::v   v:::::v  o::::o     o::::om:::::mmm::::::mmm:::::m
     v:::::v v:::::v   o::::o     o::::om::::m   m::::m   m::::m
      v:::::v:::::v    o::::o     o::::om::::m   m::::m   m::::m
       v:::::::::v     o::::o     o::::om::::m   m::::m   m::::m
        v:::::::v      o:::::ooooo:::::om::::m   m::::m   m::::m
         v:::::v       o:::::::::::::::om::::m   m::::m   m::::m
          v:::v         oo:::::::::::oo m::::m   m::::m   m::::m
           vvv            ooooooooooo   mmmmmm   mmmmmm   mmmmmm
                 (version orchestration manager)
 
              vom: command line version control tool

this project is orchestrated by vom. this means the owners and contributors
TRUST you to follow the laid out rules to ensure maximum productivity.

no worries - we'll warn you before any unnapproved moves. you can create
your own implementation with 'vom impl create --user' where you can set
your own rules and change anything you'd like. (the repository owner(s)
still have permission to delete your implementation but you'll have a
chance to copy it locally before it's gone).

commands for visitors:
vom  init  [location]  [--force]  ---------------------------------------------- create your own vom repository, pass --force to recreate it
                                                                                 if there's already one present (you need the DELETE_RECREATE
                                                                                 global permission to recreate a repository that's not yours)
     log  [implementation]  ---------------------------------------------------- see the number and history of commits on the current
                                                                                 implementation or the implementation you specify.
     impl  create  [--user]  <name>  [--force]  -------------------------------- create a new implementation in the current repository (rules
                                                                                 and contributors are not copied though). pass --force to
                                                                                 recreate it if it already exists (you need the
                                                                                 DELETE_RECREATE local permission on the implementation to
                                                                                 recreate it). passing --user skips the <name> argument and
                                                                                 sets the branch name to your username.
     impl  switch  [--user]  <name>  [--force]  -------------------------------- go to a specific implementation. command cannot be used if
                                                                                 you have uncommited changes. passing --user skips the <name>
                                                                                 argument and sets the branch name to your username.
     impl  list  --------------------------------------------------------------- get a list of all implementations on this branch along with
                                                                                 some basic info about each one.
     log  [implementation]  ---------------------------------------------------- get a list of all commits on this implementation or any
                                                                                 implementation you specify.
     user  [--contributors]  [--owners]  <username>  [implementation]  --------- get information on a user, users when names separated with a
                                                                                 comma, contributors of this repository/implementation if
                                                                                 --contributors is passed, or owners of this
                                                                                 repository/implementation if --owners is passed. results are
                                                                                 based on the specified implementation if it is passed.
     notifications  ------------------------------------------------------------ view a log of messages with timestamps and updates made to
                                                                                 your user (e.g. shouts, permission updates, ownership changes,
                                                                                 contributions, implementations, etc.)
     help  [--print]  ---------------------------------------------------------- open a window with instructions and commands. pass --print to
                                                                                 print in terminal instead.
commands for contributors:                    
vom  add  <file>  -------------------------------------------------------------- add a file or directory to the current implementation's track
                                                                                 if you have the ADD_REMOVE permission.
     commit  <message/reason>  [implementation]  [--force]  -------------------- commit changes to the current implementation or any
                                                                                 implementation you specify as long as you have the COMMIT
                                                                                 permission. pass --force to commit even with no changes and
                                                                                 create the specified implementation if it doesn't exist.
     revert  [number]  [--force]  ---------------------------------------------- revert to the last commit or the commit with the specified
                                                                                 id. pass --force to revert even with uncommited changes.
     impl  update  <implementation> [--force]  --------------------------------- replace tracked files in the current implementation with those
                                                                                 in the specified implementation. pass --force to replace even
                                                                                 with uncommited changes.
     impl  merge  <implementation>  [--force]  --------------------------------- same as 'vom impl update' but only replaces files that do not
                                                                                 exist in the current implementation.
commands for implementation owners:                    
vom  impl  perm  add  <username>  <permission>  [implementation]  -------------- add a permission to a certain user if you are an owner of the
                                                                                 implementation.
     impl  perm  remove  <username>  [--all]  <permission>  [implementation]  -- remove a permission from a certain user if you are an owner of
                                                                                 the implementation.
     impl  perm  check  <username>  [permission]  [implementation]  ------------ check if a user has a certain permission or not, or do not pass
                                                                                 a permission to get a list of their permissions.
     impl  perm  add-owner  <username>  [implementation]  ---------------------- make a user an owner of the specified implementation if you are
                                                                                 also an owner. be careful with this as implementation owners have
                                                                                 all implementation permissions, can add and remove owners, give
                                                                                 and remove permissions, or delete or recreate your implementation.
                                                                                 they cannot however remove ownership from the person who added
                                                                                 them.
     impl  perm  remove-owner  <username>  [implementation]  ------------------- remove a user's ownership of the specified implementation if you
                                                                                 are an owner. you cannot remove ownership from yourself or the
                                                                                 person who gave it to you for security reasons.
     impl  shout  <message>  [users] [implementation]  ------------------------- send a message that will appear to all implementation contributors
                                                                                 the next time they use a command in the repo or use the 
                                                                                 'vom notifications' command. only sends to the specified user(s)
                                                                                 (separated by commas) if any are provided.
commands for repository owners:
vom  perm  add  <username>  <permission>  -------------------------------------- add a permission to a certain user if you are an owner of the
                                                                                 repository.
     perm  remove  <username>  [--all]  <permission>  -------------------------- remove a permission from a certain user if you are an owner of
                                                                                 the repository.
     perm  check  <username>  [permission]  ------------------------------------ check if a user has a certain permission or not, or do not pass
                                                                                 a permission to get a list of their permissions.
     perm  add-owner  <username>  ---------------------------------------------- make a user an owner of this repository if you are
                                                                                 also an owner. be careful with this as repository owners have
                                                                                 all permissions in all implementations, can add and remove
                                                                                 owners, give and remove permissions, delete or recreate your
                                                                                 repository, and manage all implementations. they cannot however
                                                                                 remove ownership from the person who added them.
     perm  remove-owner  <username>  [implementation]  ------------------------- remove a user's ownership of the current repository if you
                                                                                 are an owner. you cannot remove ownership from yourself or the
                                                                                 person who gave it to you for security reasons.
     repo-delete  [--confirm value]  ------------------------------------------- delete the current repository if you have the DELETE_RECREATE
                                                                                 permission or are an owner of the repository. you will be
                                                                                 prompted to archive this repo instead and to enter the name of
                                                                                 the repository in the --confirm option.
     repo-archive  ------------------------------------------------------------- non-destructive alternative to 'vom repo-delete' that prevents
                                                                                 additions to tracks, commits, pushes, creation of
                                                                                 implementations and managing implementations. the repository
                                                                                 directory will persist and all commands have a warning that
                                                                                 this repository is archived and no changes can be made.
                                                                                 un-archive any time with 'vom repo-unarchive'
     repo-unarchive  ----------------------------------------------------------- revert all changes of 'vom repo-archive'
     shout  <message>  [users]  ------------------------------------------------ send a message that will appear to all users the next time they
                                                                                 use a command in the repo or use the 'vom notifications' command.
                                                                                 only sends to the specified user(s) (separated by commas) if any
                                                                                 are provided.
utility commands:
vom  --------------------------------------------------------------------------- view some basic information on vom.
     util  --clear-keys  ------------------------------------------------------- clears cached vom keys on your system. can save a few kb of space.