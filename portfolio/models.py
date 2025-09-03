from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="Optional: A screenshot of your project.")
    technologies = models.CharField(max_length=200, help_text="E.g., Django, React, PostgreSQL")
    project_url = models.URLField("Project URL", blank=True, null=True, help_text="Optional: The URL where the project is live.")
    github_url = models.URLField("GitHub URL", blank=True, null=True, help_text="Optional: The URL to the source code on GitHub.")
    display_order = models.PositiveIntegerField(default=0, help_text="Projects with lower numbers are displayed first.")

    class Meta:
        # This ensures projects are always ordered correctly when you fetch them.
        ordering = ['display_order']

    def __str__(self):
        # This provides a human-readable name in the Django admin.
        return self.title
