boRequestStatus = {
  "200": ["Success", "Successful request."],
  "400": ["Bad request", "The requested resource exists, but the request contains errors."],
  "401": ["Failed to logon or invalid session", "Logon failed. Check that the user name, password, and server name are correct. The current session may have expired. Log on to obtain a new session."],
  "403": ["Access denied", "You do not have permission to operate on the requested resource."],
  "404": ["Service is not available ", "The requested service is not provided by the RESTful Web Service SDK."],
  "405": ["Invalid request method ", "A request was made using a method that was not supported by the resource. For example, using a PUT request on a read-only resource."],
  "406": ["Not acceptable ", "The requested resource cannot generate the content type specified by the Accept attribute of the request header"],
  "408": ["BI platform server timeout", "The server timed out waiting for the request."],
  "415": ["Unsupported media type", "The request contains a media type that the server or resource does not support."],
  "500": ["RESTful web service internal error", "An unclassified error occurred. See the response body for more information."],
  "503": ["RESTful web service plugin not found", "The web service is not available. Verify that the service is configured correctly."]

}

for i in boRequestStatus:
    print(i+" :: "+boRequestStatus[i][0]+" :: "+boRequestStatus[i][1])
