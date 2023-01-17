# Product Requirement Documentation

## What is it about?
A website for travel blog + tour guide, displaying places of interest that I want to visit.

## User story
### Stage 1
1. As a visitor, I want to see a welcome page when I open it, so that I can understand what this site is all about.
2. As a visitor, I want to read travel blogs and tour guides, so that I can obtain the travel information.
3. As an admin, I want to login to the admin/management page, so that I can CRUD all the articles.
4. As an admin, I want to set visibility for each article, so that I can hide some articles from regular visitors.
5. As an admin, I want to be able to log out of the system.

### Stage 2
1. As a manager, I want to create a new account for another admin, so that I can grant admin access to other users.
2. As a manager, I want to (soft) delete an admin account, so that I can withdraw access.
3. As an admin, I can set article visibility to admin only, and articles will have three visibilities: all, only admins, only me. Because I want to have more flexibility in terms of access control.
4. As a visitor, I want to make comments on the articles, so that I can interact with the author.
5. As an admin/author, I want to reply to the comment with my name/profile, so that I can interact with the comments.

## What functionalities it will fulfill?
- [ ] Welcome page display
- [ ] Page/article navigation
- [ ] Admin login/logout
- [ ] Admin page
- [ ] Login persistence
- [ ] Article create
- [ ] Article read
- [ ] Article edit
- [ ] Article delete
- [ ] Article visibility

## System modules

### Front-end
#### Components
- Home page
  - Header
  - Footer
- Navigation bar
  - Home
  - Travel Guide
  - About Me
- Article page
  - Article preview
    - Article content
  - Pagination
  - Sidebar/Index
- About me + Contact

#### Utilities
- API wrapper
- Auth context
- i18n
- Tokens

### Back-end
- Python + Flaks + MySQL
- APIs
  - Public
    - Single article GET
    - Batch article GET
    - Token refresh
    - Login
    - Logout
  - Protected
    - Single article POST + UPDATE + DELETE