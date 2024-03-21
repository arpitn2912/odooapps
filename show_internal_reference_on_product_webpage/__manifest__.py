
{
    "name"        :"Internal Reference On Website Product",
    "author"      :"odoo demp",
    "category"    :"Website",
    "summary"     :"""Internal Reference On Product""",
    "description" :""" Internal Reference On Product """,
    "version"      :"16.0.1.0",
    "depends"     :["website_sale","website","sale_management"],
    "data"        :[
                    "views/internel_reference_template.xml",
                    "views/sale_order_view.xml"
                   ],
    "images": ["static/description/banner.png"],
    "license": "AGPL-3",
    "installable" :True,
    "application" :True,
    "auto_install":False,
}
