

{
    "name"        :"sale_order_sequence_condation",
    "author"      :"Ascetic Business Solution",
    "category"    :"Website",
    "summary"     :"""sale_order_sequence_condation""",
    
    "description" :""" sale_order_sequence_condation """,
    "version"      :"16.0.1.0",
    "depends"     :["base","sale_management"],
    "data"        :[
                    "data/ir_sequence_data.xml",
                    "views/sale_order_view.xml"
                   ],
    
    "license": "AGPL-3",
    "installable" :True,
    "application" :True,
    "auto_install":False,
}
