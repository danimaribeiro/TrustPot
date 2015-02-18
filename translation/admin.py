from django.contrib import admin
from translation.models import Language, Project
from translation.models import Template, TranslationFile, Translation
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect
import reversion
import os.path
from git import Repo
import polib
from TrustPot.settings import BASE_DIR


class LanguageAdmin(reversion.VersionAdmin):
    list_display = ('code', 'name')
    search_fields = ['name', 'code']


class ProjectAdmin(reversion.VersionAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'remote', 'status', 'save_path']}),
        (_('Languages'), {'fields': ['languages']}),
    ]
    readonly_fields = ['status', 'save_path']
    list_display = ('name', 'remote')
    search_fields = ['name']
    filter_horizontal = ['languages']
    actions = ['clone_repository', 'search_files', 'generate_translations']

    def clone_repository(self, request, queryset):
        for q in queryset:
            try:
                path_to_save = os.path.join(BASE_DIR, 'repo')
                path_to_save = os.path.join(path_to_save, q.name + '/')
                if not os.path.isdir(path_to_save):
                    Repo.clone_from(q.remote, path_to_save)
                    q.status = 'cloned'
                q.save_path = path_to_save
            except:
                q.status = 'error'
            q.save()

    def search_files(self, request, queryset):

        def visit(arg, dirname, names):
            if '.git' in names:
                names.remove('.git')
            for name in names:
                subname = os.path.join(dirname, name)
                if subname.endswith('.pot'):
                    relative = subname.replace(q.save_path, "")
                    relative = relative.replace(name, "")
                    p = Template(path=relative, name=name, project=arg,
                                 full_path=subname)
                    p.save()
                elif subname.endswith('.po'):
                    relative = subname.replace(q.save_path, "")
                    relative = relative.replace(name, "")
                    p = TranslationFile(path=relative, name=name, project=arg,
                                        full_path=subname)
                    p.save()
                print '  %s' % subname
            print

        for q in queryset:
            if q.status == 'cloned' and os.path.isdir(q.save_path):
                os.path.walk(q.save_path, visit, q)
            q.save()

    def generate_translations(self, request, queryset):
        for q in queryset:
            translation_files = TranslationFile.objects.filter(project_id=q.id)
            for translate_file in translation_files:
                potfile = polib.pofile(translate_file.full_path)
                for entry in potfile:
                    status = 'reviewed' if entry.translated() else 'not_translated'
                    t = Translation(original_text=entry.msgid,
                                translated_text=entry.msgstr, status=status,
                                original_file=translate_file)
                    t.save()


class TemplateAdmin(reversion.VersionAdmin):
    readonly_fields = ['full_path', 'path', 'name']
    list_display = ['file_name']


class TranslationFileAdmin(reversion.VersionAdmin):
    readonly_fields = ['full_path', 'path', 'name']
    list_display = ['file_name']


class TranslationAdmin(reversion.VersionAdmin):
    list_display = ['status', 'original_text', 'translated_text']
    list_filter = ['status']

    def changelist_view(self, request, extra_context=None):
        if not request.META['QUERY_STRING'] and \
            not request.META.get('HTTP_REFERER', '').startswith(request.build_absolute_uri()):
            return HttpResponseRedirect(request.path + "?status__exact=not_translated")
        return super(TranslationAdmin,self).changelist_view(request, extra_context=extra_context)


admin.site.register(Language, LanguageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(TranslationFile, TranslationFileAdmin)
admin.site.register(Translation, TranslationAdmin)
