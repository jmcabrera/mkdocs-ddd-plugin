import re
from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type


class DDDPlugin(BasePlugin):
    config_scheme = (
        ('foo', Type(str, default='a default value')),
        ('bar', Type(int, default=0)),
        ('baz', Type(bool, default=True))
    )

    cache = {}

    def on_page_context(self, context, page, nav, config, **kwargs):
        content = page.content
        if 'bounded_context' in page.meta:
            for p in nav.pages:
                if p is not page \
                        and 'bounded_context' in p.meta \
                        and p.meta['aggregate']:
                    for a in p.meta['aggregate']:
                        bc = p.meta['bounded_context']
                        # put regex matching the aggregate name.
                        # One for explicit matching ( the_context%the_name )
                        # One for implicit matching ( the_name alone. Only applied on aggregates from the same context)
                        rex = self.cache.setdefault(bc + "%" + a, {
                            'explicit': re.compile(r"(\s){}%({})(.|:|;|,|\s)".format(bc, a), re.I),
                            'implicit': re.compile(r"(\s)({})(.|:|;|,|\s)".format(a), re.I)
                        })
                        # apply at least the explicit substitution.
                        # If both pages have the same bounded context, apply implicit substitution also.
                        for r in [rex['explicit']] + ([rex['implicit']] if page.meta['bounded_context'] == bc else []):
                            content = r.sub(
                                r"\1<a href='{}' title='from {}'>\2</a>\3".format(p.abs_url, bc),
                                content)
        page.content = content
        return context

#    def on_page_content(self, html, page, files, config, **kwargs):
#        print("on_page_content")
#        print("        page is " + str(page))
#        print("        html is " + html)
#        print("             .meta = " + str(page.meta))
#        print("          .content = " + str(page.content))
#        print("        .canonical = " + str(page.canonical_url))
#        print("              .abs = " + str(page.abs_url))
#        print("       files is " + str(files))
#        print("#################################################")
#        return html + " <b>(edited)</b>"
#
#    def on_pre_build(self, config, **kwargs):
#        print("on_pre_build")
#        print("#################################################")
#
#    def on_config(self, config, **kwargs):
#        print("on_config")
#        print("          config is " + str(config))
#        print("     self.config is " + str(self.config))
#        print("#################################################")
#
#    def on_files(self, files, config, **kwargs):
#        print("on_files: files is " + str(files))
#        print("#################################################")
#
#    def on_nav(self, nav, config, **kwargs):
#        print("on_nav  : nav is " + str(nav))
#        print("#################################################")
#
#    def on_env(self, env, config, **kwargs):
#        print("on_env  : env is " + str(env))
#        print("#################################################")
#
#    def on_post_build(self, config, **kwargs):
#        print("on_post_build")
#        print("#################################################")
#
#    def on_pre_page(self, page, files, config, **kwargs):
#        print("on_pre_page")
#        print("        page is " + str(page))
#        print("             .meta = " + str(page.meta))
#        print("       files is " + str(files))
#        print("#################################################")
#
#    def on_page_markdown(self, markdown, page, files, config, **kwargs):
#        print("on_page_markdown")
#        print("        page is " + str(page))
#        print("    markdown is " + str(markdown))
#        print("    markdown is " + str(page.content))
#        print("       files is " + str(files))
#        print("#################################################")
#
#    def on_post_page(self, output, page, config, **kwargs):
#        print("on_post_page")
#        print("        page is " + str(page))
#        #print("      output is " + output)
#        print("             .meta = " + str(page.meta))
#        print("          .content = " + str(page.content))
#        print("        .canonical = " + str(page.canonical_url))
#        print("              .abs = " + str(page.abs_url))
#        print("#################################################")
#        return output + " <b>(edited)</b>"
#        print("on_post_page")
#        print("        page is " + str(page))
#        print("   " + str(page) + ".meta = " + str(page.meta))
#        print("      output is " + str(output))
#        print("#################################################")
#        return output
