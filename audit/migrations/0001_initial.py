# Generated by Django 4.1.3 on 2022-12-01 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("survey", "1014_alter_surveyuser_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Audit",
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
                    "product_name",
                    models.CharField(
                        max_length=128, verbose_name="Product / Service name"
                    ),
                ),
                (
                    "product_ref",
                    models.CharField(
                        max_length=128, verbose_name="Product / Service reference"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditByCompany",
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
                    "audit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="audit.audit"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AuditUser",
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
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=128)),
                (
                    "address_street",
                    models.CharField(max_length=128, verbose_name="Street"),
                ),
                (
                    "address_zip_code",
                    models.CharField(max_length=10, verbose_name="ZIP / Postal code"),
                ),
                ("address_city", models.CharField(max_length=64, verbose_name="City")),
                (
                    "address_country",
                    models.CharField(max_length=64, verbose_name="Country"),
                ),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "type",
                    models.CharField(
                        choices=[("AD", "Audit"), ("CS", "Customer")],
                        default="CS",
                        max_length=2,
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Active"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RQ", "Requested"),
                            ("RF", "Refused"),
                            ("VL", "Valid"),
                            ("RV", "Revoked"),
                        ],
                        default="RQ",
                        max_length=2,
                    ),
                ),
                ("validation_date", models.DateField(blank=True, null=True)),
                ("revocation_date", models.DateField(blank=True, null=True)),
                (
                    "validate_by_company",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="audit.company",
                    ),
                ),
                (
                    "validate_by_user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="audit.audituser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="audituser",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="audit.company"
            ),
        ),
        migrations.AddField(
            model_name="audituser",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="AuditByUser",
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
                    "audit_by_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="audit.auditbycompany",
                    ),
                ),
                (
                    "audit_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="audit.audituser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="auditbycompany",
            name="audit_company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="audit.company"
            ),
        ),
        migrations.AddField(
            model_name="audit",
            name="certificate",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="audit.certificate",
            ),
        ),
        migrations.AddField(
            model_name="audit",
            name="survey_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="survey.surveyuser"
            ),
        ),
        migrations.AddConstraint(
            model_name="auditbyuser",
            constraint=models.UniqueConstraint(
                fields=("audit_by_company", "audit_user"), name="unique_auditByUser"
            ),
        ),
        migrations.AddConstraint(
            model_name="auditbycompany",
            constraint=models.UniqueConstraint(
                fields=("audit", "audit_company"), name="unique_auditByCompany"
            ),
        ),
    ]
