import boto
from boto.exception import BotoServerError

class CloudSearch(object):

    def __init__(self,
                 aws_access_key_id=None,
                 aws_secret_access_key=None,
                 domain_name=None):

        self.conn = None
        self.domain = None
        if aws_access_key_id and aws_secret_access_key:
            self.connect_to_cs(aws_access_key_id,aws_secret_access_key)
            if domain_name:
                self.lookup_domain(domain_name)

    def connect_to_cs(self,
                      aws_access_key_id,
                      aws_secret_access_key):
        '''
            Initialize the base cloudsearch connection.  This is a lazy loaded
            function, so it will always succeed until we do a domain lookup
        '''
        self.conn = None

        # establish connection with cloudsearch
        self.conn = boto.connect_cloudsearch(aws_access_key_id,
                                        aws_secret_access_key)

    def lookup_domain(self, domain_name):
        '''
        Attach this object to a cloudsearch domain and create all class member
        variables for use later.

        Returns True on success
        '''
        if not self.conn:
            print 'Not connected to cloudsearch - use connect_to_cs()'
            return None

        self.domain = None
        self.doc_service = None
        self.search_service = None

        try:
            # fetch domain
            self.domain = self.conn.lookup(domain_name)
            if not self.domain:
                # did not find the domain
                print 'No domain found with name %s' % domain_name
                return None
        except BotoServerError as e:
            '''
                These errors generaly look like:
                BotoServerError: 403 Forbidden
                <ErrorResponse xmlns="http://cloudsearch.amazonaws.com/doc/2011-02-01/">
                  <Error>
                    <Type>Sender</Type>
                    <Code>InvalidClientTokenId</Code>
                    <Message>The security token included in the request is invalid.</Message>
                  </Error>
                  <RequestId>8c1e7d9c-9fcc-11e3-a9bf-xxxxxxxx</RequestId>
                </ErrorResponse>
            '''
            print e
            return None

        #self.doc_service = self.domain.get_document_service()
        #self.search_service = self.domain.get_search_service()

        return True

    def create_domain(self,domain_name):
        '''
            Used to create a new cloudsearch domain.  Note this should
            be seldom used since each new domain created will return a new
            endpoint which all clients would have to be updated with the
            new information.
        '''
        if not self.conn:
            print 'Not connected to cloudsearch - use connect_to_cs()'
            return None

        if self.domain:
            # domain already attached to this
            print 'Domain already associated with this class instance object'
            return None

        if self.lookup_domain(domain_name):
            print 'Domain with name: %s already exists' % domain_name
            return None

        # Create the domain
        # Side note - if a domain already exists with this name, it is merely
        # returned
        self.domain = self.conn.create_domain(domain_name)

        return True

    def populate_schema(self, schema):
        '''
            Create the index fields for a domain according to the schema json
            doc.  The schema should be a list of field objects.  The archtype:
            {
                # Required fields
                'field_name': '',
                'field_type': 'literal|text|uint', # one of literal|text|uint

                # Optional fields
                'field_default' : None,   #
                'field_source' : None,    # pull value from source document using this field name

                # if type is unit
                'field_default' = 0 # or some decimal
                # No options - everything is true
                # if type is text
                'field_facet': 'False',   # Facets can be calculated for filtering
                'field_result': 'True',   # Results can include content for this field
                # if type is literal
                'field_search': 'False',  # Can the field be searched?
                'field_facet': 'False',   # Facets can be calculated for filtering
                'field_result': 'True',   # Results can include content for this field
            }
            There are lots of special rules for combinations of these fields
            that are not documented here.  Check the AWS Cloudsearch documentation

        '''
        if not self.conn:
            print 'Not connected to cloudsearch - use connect_to_cs()'
            return None

        if not self.domain:
            # no domain  attached to this instance
            print 'No Domain associated with this class instance object'
            return None

        for field in schema:
            try:
                print 'adding field: %s' % field['field_name']
                f = self.domain.create_index_field(
                    field['field_name'], # required field
                    field['field_type'], # required field
                    default=field.get('field_default',None),
                    facet=field.get('field_facet',False),
                    result=field.get('field_result',False),
                    searchable=field.get('field_search',False),
                    source_attributes=field.get('field_source')
                    )
            except Exception as e:
                print 'Exception: %s' % e
                return None

        return True

'''
        # define version number as epoch time in secs
        version = calendar.timegm(time.gmtime())
'''