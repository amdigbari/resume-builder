# Generated by Django 5.0.6 on 2024-07-05 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("template", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="instance created at",
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="latest update at",
                        verbose_name="updated at",
                    ),
                ),
                (
                    "is_template",
                    models.BooleanField(
                        default=False,
                        help_text="is resume a template",
                        verbose_name="is template",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="resume's title",
                        max_length=100,
                        null=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False,
                        help_text="is resume public",
                        verbose_name="is public",
                    ),
                ),
                (
                    "forked_from",
                    models.ForeignKey(
                        blank=True,
                        help_text="resume forked from",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="forks",
                        to="resume.resume",
                        verbose_name="forked from",
                    ),
                ),
                (
                    "template",
                    models.OneToOneField(
                        help_text="resume's template",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="template.template",
                        verbose_name="template",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="resume's user",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="resumes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ResumeSection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="instance created at",
                        verbose_name="created at",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="latest update at",
                        verbose_name="updated at",
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="resume section's content", verbose_name="content"
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        blank=True,
                        help_text="section's resume",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sections",
                        to="resume.resume",
                        verbose_name="resume",
                    ),
                ),
                (
                    "section",
                    models.OneToOneField(
                        help_text="resume section's section",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="template.section",
                        verbose_name="section",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddConstraint(
            model_name="resume",
            constraint=models.UniqueConstraint(
                fields=("user", "title"), name="title_must_be_unique_per_user"
            ),
        ),
    ]
