
# ProjectName - BlogNest  
## Summary

BlogNest is a versatile blogging platform that empowers bloggers to create and share their content effectively. It provides essential features for bloggers to streamline their blogging experience and grow their online presence. Whether you're a seasoned blogger or just starting, BlogNest has you covered.

## Key Features

1. Content Creation: Write and publish your blog posts with ease. The platform provides a user-friendly editor to craft your content.

2. Sharing: Share your blog posts with your audience and on social media platforms to increase your reach.

3. Commenting: Engage with your readers through comments. Encourage discussions and gather feedback.

4. UserProfile Management: Customize your profile, add a bio, profile picture, and manage your blog posts.

5. Edit & Delete Blog Contents: Easily edit and delete your published blog posts to keep your content up to date.

6. Edit & Delete Comments: Have control over the comments on your blog posts. Edit or remove them as needed.

7. likes: Keep track of the number of views on your blog posts to understand their popularity.

8. Authorizations: Implement user roles and permissions for different levels of access and control.

## Prerequisites
Before running the BlogNest application, make sure you have the following prerequisites installed on your system:

1. PostgreSQL (or your preferred database, not required for local development)
2. Django (Python web framework)


## Setup

To run the BlogNest application on your system, please ensure the following:

1. Clone the Repository
  ```
  git clone https://github.com/Subash0711/blogNest.git

  ```

2. Create a Virtual Environment (optional but recommended)
  ```
  python -m venv venv  

  source venv/bin/activate (for linux)  
  # OR
  venv\Scripts\activate  (for Windows)

  cd blog/blog_project
  ```
3. Then run the following command to install all required Python packages

  ```
  pip install -r requirements.txt
  ```
4. After installing the dependencies, run the migration commands to set up your database schema
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
5. Finally, start the development server with the following command
  ```
  python manage.py runserver
  ```

Access the BlogNest application in your web browser at http://localhost:8000/.

## Errors

```  
  django.db.utils.OperationalError: no such table: blog_users
  [05/Oct/2024 12:05:39] "POST /Blog-nest/Signup HTTP/1.1" 500 168711
  Not Found: /Blog-nest/undefined
```

To resolve this, remove `the blog/blog_project/db.sqlite3` file from your project, and then follow the setup steps in step 4."

Start creating, sharing, and managing your blog content on BlogNest!

