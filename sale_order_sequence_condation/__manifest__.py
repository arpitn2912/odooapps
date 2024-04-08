

{
    "name"        :"sale_order_sequence_condation",
    "author"      :"Aon",
    "category"    :"Website",
    "summary"     :"""sale_order_sequence_condation""",
    
    "description" :""" sale_order_sequence_condation """,
    "version"      :"16.0.1.0",
    "depends"     :["base","sale_management"],
    "data"        :[
                    "data/ir_sequence_data.xml",
                    "views/sale_order_view.xml"
                   ],
  
    "installable" :True,
    "application" :True,
    "auto_install":False,
}
