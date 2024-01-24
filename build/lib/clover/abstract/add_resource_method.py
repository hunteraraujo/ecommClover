"""Resource Method Decorator

Creates methods that hit endpoints of the form: /v1/{resource}/{id}/name
"""


def add_resource_method(name, http_verb, http_path=None):
    """Class decorator to add a method."""

    # Default path is the method name.
    if http_path is None:
        http_path = name

    def wrapper(cls):

        # Define the method.
        def resource_request(cls, sid, **params):

            json_body = None
            query_params = None


            if http_verb.lower() in set(['post', 'put']):
                # Set as JSON in body.
                json_body = params

                return cls.request(
                    method=http_verb,
                    path=[sid, http_path],
                    json=json_body
                )
            else:
                # Set as url query parameters.
                query_params = params
                return cls.request(
                    method=http_verb,
                    path=[sid, http_path],
                    params=query_params
                )

        # Add the method to the class.
        setattr(cls, name, classmethod(resource_request))
        
        return cls

    return wrapper