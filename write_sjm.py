# =============================================================================
# Filename: write_sjm.py
# Version: 1.0
# Author: Kai Yu - finno@live.cn
# https://github.com/readline
# Last modified: 2017-01-16 15:18
# Description: 
# 
# =============================================================================
def write_sjm(savepath, cmd, jobid, queue='all.q', memory=8, cpu=8, io=None, proj=None, init=False, over=False, env=None, dir=None, after=None):
    if init == True and over == False:
        savefile = open(savepath, 'w')
        savefile.write('<Task>\n')
        if env:
            savefile.write('<Env>%s</Env>\n'%env)
        savefile.write('<Job>\n')
        savefile.write('    <jobid>%s</jobid>\n'%jobid)
        savefile.write('    <queue>%s</queue>\n'%queue)
        savefile.write('    <memory>%.1f</memory>\n'%memory)
        savefile.write('    <cpu>%d</cpu>\n'%cpu)
        if io:
            savefile.write('    <io>%d</io>\n'%io)
        if proj:
            savefile.write('    <proj>%s</proj>\n'%proj)
        if dir:
            savefile.write('    <dir>%s</dir>\n'%dir)
        if after:
            savefile.write('    <after>%s</after>\n'%after)
        savefile.write('    <cmd>\n        %s\n    </cmd>\n'%(cmd.strip().replace('\n','\n        ')))
        savefile.write('</Job>\n')
    elif init == False and over == True:
        savefile = open(savepath, 'a')
        savefile.write('<Job>\n')
        savefile.write('    <jobid>%s</jobid>\n'%jobid)
        savefile.write('    <queue>%s</queue>\n'%queue)
        savefile.write('    <memory>%.1f</memory>\n'%memory)
        savefile.write('    <cpu>%d</cpu>\n'%cpu)
        if io:
            savefile.write('    <io>%d</io>\n'%io)
        if proj:
            savefile.write('    <proj>%s</proj>\n'%proj)
        if dir:
            savefile.write('    <dir>%s</dir>\n'%dir)
        if after:
            savefile.write('    <after>%s</after>\n'%after)
        savefile.write('    <cmd>\n        %s\n    </cmd>\n'%(cmd.strip().replace('\n','\n        ')))
        savefile.write('</Job>\n')
        savefile.write('</Task>')
    elif init == False and over == False:
        savefile = open(savepath, 'a')
        savefile.write('<Job>\n')
        savefile.write('    <jobid>%s</jobid>\n'%jobid)
        savefile.write('    <queue>%s</queue>\n'%queue)
        savefile.write('    <memory>%.1f</memory>\n'%memory)
        savefile.write('    <cpu>%d</cpu>\n'%cpu)
        if io:
            savefile.write('    <io>%d</io>\n'%io)
        if proj:
            savefile.write('    <proj>%s</proj>\n'%proj)
        if dir:
            savefile.write('    <dir>%s</dir>\n'%dir)
        if after:
            savefile.write('    <after>%s</after>\n'%after)
        savefile.write('    <cmd>\n        %s\n    </cmd>\n'%(cmd.strip().replace('\n','\n        ')))
        savefile.write('</Job>\n')
    else:
        savefile = open(savepath, 'w')
        savefile.write('<Task>\n')
        if env:
            savefile.write('<Env>%s</Env>\n'%env)
        savefile = open(savepath, 'a')
        savefile.write('<Job>\n')
        savefile.write('    <jobid>%s</jobid>\n'%jobid)
        savefile.write('    <queue>%s</queue>\n'%queue)
        savefile.write('    <memory>%.1f</memory>\n'%memory)
        savefile.write('    <cpu>%d</cpu>\n'%cpu)
        if io:
            savefile.write('    <io>%d</io>\n'%io)
        if proj:
            savefile.write('    <proj>%s</proj>\n'%proj)
        if dir:
            savefile.write('    <dir>%s</dir>\n'%dir)
        if after:
            savefile.write('    <after>%s</after>\n'%after)
        savefile.write('    <cmd>\n        %s\n    </cmd>\n'%(cmd.strip().replace('\n','\n        ')))
        savefile.write('</Job>\n')
        savefile.write('</Task>')

