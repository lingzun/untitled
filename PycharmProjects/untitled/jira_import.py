#!/usr/bin/env python3
#coding:utf-8
import re
from jira import JIRA
class Jira_import(object):
    def __init__(self):
        self.server = 'http://bug.chenyee.com:8080/'
        self.jiraClinet = None
    def jira_login(self,accout,passwd):
        self.jiraClinet = JIRA(server=self.server, basic_auth=(accout, passwd))
        if self.jiraClinet != None:
            return True
        else:
            return False
    def bug_post(self,summary,description,tool_version,assignee_name,priority='2',project_id='10002',issuetype_name='故障',components='10115'):
            bug_detail={
                "project": {"id": project_id},
                "summary": summary,
                "description": description,
                'issuetype': {'name': issuetype_name},
                "components":components,
                "priority":{"id":priority},
                "customfield_10008":tool_version,
                'assignee':{'name': assignee_name},
                'components': [{'id': components}],
                "customfield_10012":{'id':"10034"},
             }
            self.jiraClinet.create_issue(fields=bug_detail)
    def bug_modify(self,summary_old,description_old,summary_new,id):
            issue=self.jiraClinet.issue(str('SW17W16A-'+id))
            issue.update(summary=summary_new,description=description_old)
            # issue_dict = {
            #     'summary': summary_old,
            #     'description': description_old,
            # }
            # self.jiraClinet.update(fields=issue_dict)




