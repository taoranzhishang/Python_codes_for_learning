from string import Template

print(type(Template))  # <class 'string._TemplateMetaclass'>
str = Template("hello,$name是$what")
print(str.substitute(name='我', what='sb'))
