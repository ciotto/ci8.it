import os
import re
import requests
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render_to_response
from django.template import RequestContext
from staticsites.decorators import staticview
from markdown2 import Markdown


markdowner = Markdown(extras=['tables', 'fenced-code-blocks', 'code-friendly'])


def html_from_markdown_url(url, skip_title=1):
    if url.startswith('http://') or url.startswith('https://'):
        base_url = os.path.dirname(url)
        base_image_url = base_url

        response = requests.get(url)
        content = response.content
    else:
        base_url = settings.BASE_REPO_URL + os.path.dirname(url)
        base_image_url = settings.BASE_REPO_IMAGE_URL + os.path.dirname(url)

        with open(url, 'r') as f:
            content = f.read()
    content = '\n'.join(content.split('\n', skip_title)[skip_title:])
    content = re.sub(re.compile(r'!\[(.+)\]\((?!http)(.+)\)', re.MULTILINE), r'![\1](' + base_image_url + r'/\2)', content)
    content = re.sub(re.compile(r'\[(.+)\]\((?!http)(.+)\)', re.MULTILINE), r'[\1](' + base_url + r'/\2)', content)
    content = markdowner.convert(content)
    content = content.replace('<table>', '<div class="table-responsive"><table>')
    content = content.replace('</table>', '</table></div>')
    return content


# Pages
home_page = {
    'title': 'Home',
    'path': 'index.html',
    'date': '2019-04-18',
    'lastmod': '2020-01-17',
    'changefreq': 'monthly',
    'priority': 1,
}
about_me_page = {
    'title': 'About me',
    'path': 'about.html',
    'date': '2019-04-18',
    'lastmod': '2019-04-18',
    'changefreq': 'monthly',
    'priority': 0.9,
}
haier_t32x_page = {
    'title': 'Haier T32X robot',
    'path': 'haier-t32x.html',
    'date': '2019-04-18',
    'lastmod': '2019-04-18',
    'changefreq': 'monthly',
    'priority': 0.8,
    'md': html_from_markdown_url('https://raw.githubusercontent.com/ciotto/teardown/master/haier-t32x/README.md'),
    'description': 'Reverse engineering the Haier T325 Cleaning Robot.',
    'og_image': 'http://ci8.it%s' % static('/ci8/images/share/haier_t32x.jpg'),
    'tags': [
        ('reversing', 'Reversing'),
        ('stm32', 'STM32'),
        ('swd', 'SWD'),
        ('uart', 'UART'),
        ('st-link', 'ST-Link'),
        ('openocd', 'OpenOCD'),
        ('hardware-security', 'Hardware Security'),
        ('gdb', 'GDB'),
    ]
}
digipass_go_6_page = {
    'title': 'DIGIPASS GO 6',
    'path': 'digipass-go-6.html',
    'date': '2019-04-18',
    'lastmod': '2019-04-18',
    'changefreq': 'monthly',
    'priority': 0.8,
    'md': html_from_markdown_url('https://raw.githubusercontent.com/ciotto/teardown/master/digipass-go-6/README.md'),
    'description': 'Reverse engineering the Vasco DIGIPASS GO 6.',
    'og_image': 'http://ci8.it%s' % static('/ci8/images/share/digipass_go_6.jpg'),
    'tags': [
        ('reversing', 'Reversing'),
    ]
}
multiple_choice_test_omr_page = {
    'title': 'Multiple Choice Test OMR',
    'path': 'multiple-choice-test-omr.html',
    'date': '2020-01-17',
    'lastmod': '2020-01-17',
    'changefreq': 'monthly',
    'priority': 0.8,
    'md': html_from_markdown_url('sites/ci8/multiple_choice_test_omr/README.md'),
    'description': 'Making an OMR for a generic multiple choice test, step by step, using OpenCV and Python.',
    'og_image': 'http://ci8.it%s' % static('/ci8/images/share/multiple_choice_test_omr.jpg'),
    'tags': [
        ('omr', 'OMR'),
        ('opencv', 'OpenCV'),
        ('python', 'Python'),
    ]
}
mod_wsgi_error_page = {
    'title': 'Apache mod_wsgi/psycopg2 error',
    'path': 'mod-wsgi-error.html',
    'date': '2019-04-26',
    'lastmod': '2019-04-26',
    'changefreq': 'monthly',
    'priority': 0.8,
    'md': html_from_markdown_url('sites/ci8/mod_wsgi_error/README.md'),
    'description': 'mod_wsgi: Truncated or oversized response headers received from daemon process.',
    'og_image': 'http://ci8.it%s' % static('/ci8/images/share/mod_wsgi_error.jpg'),
    'tags': [
        ('apache', 'Apache'),
        ('wsgi', 'WSGI'),
        ('python', 'Python'),
        ('gdb', 'GDB'),
    ]
}
tags_page = {
    'title': 'Tags',
    'path': 'tags.html',
    'date': '2019-04-26',
    'lastmod': '2020-01-17',
    'changefreq': 'monthly',
    'priority': 0.8,
}
cookies_policy_page = {
    'path': 'cookies-policy.html',
    'date': '2020-01-17',
    'lastmod': '2020-01-17',
    'changefreq': 'yearly',
    'priority': 0.7,
    'cookies': {
        'needed': [
            {

                'name': 'EU_COOKIE_LAW_CONSENT',
                'provider': '.ci8.it',
                'purpose': 'Stores the consent status of the user\'s cookies for the current domain.',
                'expiration': '1 year',
            },
        ],
        'preferences': [
        ],
        'statistics': [
            {
                'name': '_ga',
                'provider': '.ci8.it',
                'purpose': 'Register a unique ID used to generate statistical data on how the visitor uses the website.',
                'expiration': '2 years',
            },
            {
                'name': '_gat',
                'provider': '.ci8.it',
                'purpose': 'Used by Google Analytics to limit the frequency of requests.',
                'expiration': '1 day',
            },
            {
                'name': '_gid',
                'provider': '.ci8.it',
                'purpose': 'Register a unique ID used to generate statistical data on how the visitor uses the website.',
                'expiration': '1 day',
            },
        ],
        'marketing': [
        ],
    }
}
pages = [
    home_page,
    about_me_page,
]


@staticview(path=home_page['path'])
def index(request):
    ctx = dict(home_page)
    ctx.update({
        'title': None,
        'pages': pages,
        'articles': [
            multiple_choice_test_omr_page,
            haier_t32x_page,
            digipass_go_6_page,
        ]
    })

    return render_to_response('ci8/index.html', ctx, context_instance=RequestContext(request))


@staticview(path=about_me_page['path'])
def about_me(request):
    ctx = dict(about_me_page)
    ctx.update({
        'title': 'Christian Bianciotto',
        'pages': pages,
    })

    return render_to_response('ci8/about.html', ctx, context_instance=RequestContext(request))


@staticview(path=haier_t32x_page['path'])
def haier_t32x(request):
    ctx = dict(haier_t32x_page)
    ctx.update({
        'pages': pages,
    })

    return render_to_response('ci8/md.html', ctx, context_instance=RequestContext(request))


@staticview(path=digipass_go_6_page['path'])
def digipass_go_6(request):
    ctx = dict(digipass_go_6_page)
    ctx.update({
        'pages': pages,
    })

    return render_to_response('ci8/md.html', ctx, context_instance=RequestContext(request))


@staticview(path=multiple_choice_test_omr_page['path'])
def multiple_choice_test_omr(request):
    ctx = dict(multiple_choice_test_omr_page)
    ctx.update({
        'pages': pages,
    })

    return render_to_response('ci8/md.html', ctx, context_instance=RequestContext(request))


@staticview(path=mod_wsgi_error_page['path'])
def mod_wsgi_error(request):
    ctx = dict(mod_wsgi_error_page)
    ctx.update({
        'pages': pages,
    })

    return render_to_response('ci8/md.html', ctx, context_instance=RequestContext(request))


@staticview(path=tags_page['path'])
def tags(request):
    tags = {}
    for page in pages:
        if 'tags' in page:
            for tag_slug, tag_name in page['tags']:
                if tag_slug not in tags:
                    tags[tag_slug] = {
                        'slug': tag_slug,
                        'name': tag_name,
                        'pages': []
                    }
                tags[tag_slug]['pages'].append(page)

    ctx = dict(tags_page)
    ctx.update({
        'tags': tags,
    })

    return render_to_response('ci8/tags.html', ctx, context_instance=RequestContext(request))


@staticview(path=cookies_policy_page['path'])
def cookies_policy(request):
    ctx = cookies_policy_page

    return render_to_response('cookies/cookies.html', ctx)


@staticview(path='sitemap.xml')
def sitemap(request):
    ctx = {
        'pages': pages + [tags_page, cookies_policy_page],
    }

    return render_to_response('ci8/sitemap.xml', ctx, content_type='application/xml')
