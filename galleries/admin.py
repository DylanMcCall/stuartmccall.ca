from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from orderable.admin import OrderableAdmin, OrderableTabularInline

from common.utils import compress_image

from galleries import models


class PortfolioGalleryInline(OrderableTabularInline):
    model = models.PortfolioGallery
    verbose_name = _("gallery")
    verbose_name_plural = _("contents")
    extra = 0
    fields = (
        'sort_order',
        'gallery_preview',
        'portfolio',
        'gallery',
    )
    readonly_fields = (
        'gallery_preview',
    )

    def gallery_preview(self, obj):
        if obj.gallery:
            return _image_preview(obj.gallery.featured_thumbnail)
        else:
            return None


class GalleryMediaInline(OrderableTabularInline):
    model = models.GalleryMedia
    verbose_name = _("media item")
    verbose_name_plural = _("contents")
    extra = 0
    fields = (
        'sort_order',
        'media_preview',
        'gallery',
        'media',
    )
    readonly_fields = (
        'media_preview',
    )
    raw_id_fields = (
        'gallery',
        'media',
    )

    def media_preview(self, obj):
        if obj.media:
            return _image_preview(obj.media.featured_thumbnail)
        else:
            return None


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'site')
    list_filter = (
        'site',
    )
    inlines = [
        PortfolioGalleryInline,
    ]


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'gallery_preview',)
    inlines = [
        GalleryMediaInline,
    ]

    def gallery_preview(self, obj):
        return _image_preview(obj.featured_thumbnail)


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_preview', 'title',)
    list_filter = (
        'media_type',
    )

    def media_preview(self, obj):
        return _image_preview(obj.featured_thumbnail)


def _image_preview(image, size=80):
    if image:
        image_dict = compress_image(image, width=80, height=80, crop='center', quality=95)
    else:
        return None

    if image_dict:
        image_default = image_dict.get('default', {})
        srcset = []

        for image_variant in image_dict.get('sizes'):
            srcset.append('{src} {x}'.format(
                src=image_variant.get('src'),
                x=image_variant.get('x')
            ))

        style = 'height: {size}; width: auto'.format(size=size)

        return format_html('<img class="admin-preview" src="{src}" width="{width}" height="{height}" srcset="{srcset}" style="{style}" />',
            src=image_default.get('src'),
            width=image_default.get('width'),
            height=image_default.get('height'),
            srcset=str(', ').join(srcset),
            style=style
        )
    else:
        return None
