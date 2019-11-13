from django.contrib import admin
from Articles.models import Author, Category, Article, Comment

admin.site.register(Category)

@admin.register(Article) 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author', 'timestamp', 'status')  
    list_filter = ('status', 'categories','timestamp',)
    search_fields = ['title','author__author_name','categories__category_title']
    actions = ['make_published']

    def make_published(self, request, queryset):
    	rows_updated = queryset.update(status='p')
    	if rows_updated == 1:
    		message_bit = "1 article was"
    	else:
    		message_bit = "%s articles were" %rows_updated
    	self.message_user(request, "%s succesfully marked as published" % message_bit)
    make_published.short_description = "Mark selected articles as published"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'post', 'timestamp')
	list_filter = ('timestamp',)
	search_fields = ['user__username','post__title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	fieldsets = (          
        ('Personal Information', {
        	'classes': ('wide', 'extrapretty'),
            'fields': ('author_name', 'profile_picture', 'about_author')
        }),
        ('Websites or Social accounts (OPTIONAL)', {
        	
        	'classes': ('collapse','wide', 'extrapretty',),
            'fields': ('website', 'linkedin','facebook','insta','others')
        }),
    )
    

