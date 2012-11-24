import hashlib

def preTemplate(page, templ_vars):
        if len(templ_vars['page']['subpages']) > 0:
                for subpage in templ_vars['page']['subpages']:
                        if 'gravatar' in subpage:
                                print 'gravatar found'
                                m = hashlib.md5()
                                m.update(subpage['gravatar'].strip().lower())
                                subpage['gravatarmd5'] = m.hexdigest()


hooks = {
  'page.template.pre': [preTemplate]
}
