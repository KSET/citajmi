import logging
import httpagentparser
import re


class LoggingMiddleware(object):

    def process_response(self, request, response):
        # 'browser': {'name': 'Chrome', 'version': '24.0.1312.57'},
        # 'flavor': {'name': 'MacOS', 'version': 'X 10.7.5'},
        # 'os': {'name': 'Macintosh'}
        try:
            agent = httpagentparser.detect(request.META['HTTP_USER_AGENT'])
            agent_info = '"%s %s"' % (agent['browser'].get('name', '-'), agent['browser'].get('version', '-'))
        except:
            agent_info = '-'
        entry = ('%s "%s %s" %s %s %s' % (request.META.get('REMOTE_ADDR', '-'), request.method, request.path,
                                          response.status_code, len(response.content), agent_info))

        logger = logging.getLogger('simplelogger')
        code = str(response.status_code)
        if re.search(r'4[\d]{2}', code):    # 4xx warning
            logger.warning(entry)
        elif re.search(r'5[\d]{2}', code):  # 5xx error
            logger.error(entry)
        else:
            logger.info(entry)

        return response
