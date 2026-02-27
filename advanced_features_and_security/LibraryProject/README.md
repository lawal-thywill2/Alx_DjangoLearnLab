PERMISSIONS AND GROUPS SETUP

Custom permissions were added to the Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups created in Django Admin:
- Viewers: can_view
- Editors: can_create, can_edit
- Admins: all permissions

Views are protected using @permission_required decorator:
- view_books requires can_view
- create_book requires can_create
- edit_book requires can_edit
- delete_book requires can_delete

Users are assigned to groups using Django Admin.
Permissions are enforced automatically based on group membership.