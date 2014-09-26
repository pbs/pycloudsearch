from pycs import CloudSearch

aws_access_key_id='key here'
aws_secret_access_key='secret here'

'''
return_fields = geoprofile,mediafiles,mime_type,rating,version,destination,guid,program_description,program_slug,series_guid,season_guid,keywords,modified_epoch,modified_datetime,airdate_datetime,airdate_epoch,expire_datetime,expire_epoch,nola_root,nola_episode,availability,program,type,title,tpmid,length,producer,uri_mezzanine,uri_thumbnail,image,uri,series,season,program_uri,program_image,encoding,captions,producer_program_slug,topics,description
stop_fields = episode,hour,season,series,segment,classic,theater
'''
schema = [
    {
        'field_name': 'airdate_datetime',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': False,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',   #
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'airdate_epoch',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },
    {
        'field_name': 'availability',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'captions',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'description',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'description_short',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'encoding',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'expire_datetime',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': False,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'expire_epoch',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },
    {
        'field_name': 'f_availability',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'availability'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_captions',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'captions'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_destination',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'destination'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_encoding',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'encoding'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_geo_restriction_cc',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'geo_restriction_cc'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_geo_restriction_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'geo_restriction_type'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_mime_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'mime_type'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_nola_root',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'nola_root'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_object_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'object_type'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_producer',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'producer'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_program',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'program'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_program_slug',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'program_slug'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_rating',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'rating'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_topics',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'topics'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'f_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': True,   # Facets can be calculated for filtering
        'field_result': False,   # Results can include content for this field
        'field_default' : '',
        'field_source' : [{'source_data_copy': {'source_name': 'type'},'source_data_function': 'Copy'}],    # pull value from source document using this field name
    },
    {
        'field_name': 'geo_restriction_cc',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'geo_restriction_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'guid',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'image',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'keywords',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'length',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },
    {
        'field_name': 'mediafiles',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'mime_type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'modified_datetime',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': False,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'modified_epoch',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },
    {
        'field_name': 'nola_episode',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'nola_root',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'producer',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'program',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'program_description',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'program_slug',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'program_url',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'rating',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'title',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'topics',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'tpmid',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },
    {
        'field_name': 'type',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'uri',
        'field_type': 'text', # one of literal|text|uint
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'url',
        'field_type': 'literal', # one of literal|text|uint
        'field_search': True,  # Can the field be searched?
        'field_facet': False,   # Facets can be calculated for filtering
        'field_result': True,   # Results can include content for this field
        'field_default' : '',
        'field_source' : None,    # pull value from source document using this field name
    },
    {
        'field_name': 'version',
        'field_type': 'uint', # one of literal|text|uint
        'field_default' : 0
    },

]

cs = pyCloudSearch(aws_access_key_id,aws_secret_access_key,'edgar-test3')

cs.populate_schema(schema)
