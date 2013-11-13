__author__  = 'LouK'
__version__ = '1.0'


import b3, random, time, thread, threading, re, string
from threading import Timer
import b3.events
import b3.plugin

#--------------------------------------------------------------------------------------------------
class RandomGuns:
    items                  = ['D', 'E', 'C', 'A', 'F']

class Guns:
    weapon                  = 0

class GungamePlugin(b3.plugin.Plugin):
    requiresConfigFile = False
    _clientvar_name = 'gun_info'
    _clientvar = ''
    _clientweap = 0
    _delay = 2.6
    _guns =  ['C', 'G', 'H', 'D', 'S', 'J', 'E', 'O', 'Q', 'I', 'N', 'F']
        
    def onStartup(self):
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False
        
        self.registerEvent(b3.events.EVT_CLIENT_KILL)
        self.registerEvent(b3.events.EVT_GAME_EXIT)
        self.registerEvent(b3.events.EVT_GAME_ROUND_START)
        self._adminPlugin.registerCommand(self, 'gun', 40, self.cmd_gun)
    
    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_KILL: 
            self.someoneKilled(event.client, event.target, event.data)
            self.someoneDied(event.target, event.client, event.data)
        if event.type == b3.events.EVT_GAME_EXIT:
            self.console.write('fraglimit 0')
        if event.type == b3.events.EVT_GAME_ROUND_START:
            random.shuffle(self._guns)
        
    def someoneDied(self, client, target, data=None):
        client.setvar(self, self._clientvar, client.cid)
        weap2 = self.get_gun_stats(client)
        if (data[1] == self.console.UT_MOD_KNIFE):
            if weap2.weapon > 0:
                if ((weap2.weapon % 2) == 0):
                    if weap2.weapon == 2:
                        weap2.weapon -= 2
                    else:
                        weap2.weapon -= 3
                else:
                    if weap2.weapon == 1:
                        weap2.weapon -= 1
                    else:
                        weap2.weapon -= 2
        t = threading.Timer(self._delay, self.giveWeapon, args=[client])
        t.start() 

    def giveWeapon(self, client):
        weap2 = self.get_gun_stats(client)
        if weap2.weapon==0:
            weapon='B'
        elif weap2.weapon==1:
            weapon=self._guns[0]
        elif weap2.weapon==2:
            weapon=self._guns[0]
        elif weap2.weapon==3:
            weapon=self._guns[1]
        elif weap2.weapon==4:
            weapon=self._guns[1]
        elif weap2.weapon==5:
            weapon=self._guns[2]
        elif weap2.weapon==6:
            weapon=self._guns[2]
        elif weap2.weapon==7:
            weapon=self._guns[3]
        elif weap2.weapon==8:
            weapon=self._guns[3]
        elif weap2.weapon==9:
            weapon=self._guns[4]
        elif weap2.weapon==10:
            weapon=self._guns[4]
        elif weap2.weapon==11:
            weapon=self._guns[5]
        elif weap2.weapon==12:
            weapon=self._guns[5]
        elif weap2.weapon==13:
            weapon=self._guns[6]
        elif weap2.weapon==14:
            weapon=self._guns[6]
        elif weap2.weapon==15:
            weapon=self._guns[7]
        elif weap2.weapon==16:
            weapon=self._guns[7]
        elif weap2.weapon==17:
            weapon=self._guns[8]
        elif weap2.weapon==18:
            weapon=self._guns[8]
        elif weap2.weapon==19:
            weapon=self._guns[9]
        elif weap2.weapon==20:
            weapon=self._guns[9]
        elif weap2.weapon==21:
            weapon=self._guns[10]
        elif weap2.weapon==22:
            weapon=self._guns[10]
        elif weap2.weapon==23:
            weapon=self._guns[11]
        elif weap2.weapon==24:
            weapon=self._guns[11]
        elif weap2.weapon==25:
            weapon=self._guns[11]
        elif weap2.weapon==26:
            weapon=self._guns[11]
            weap2.weapon -= 3
        self.console.write('gw %s A%s-@' % (client.cid, weapon))
        
    def init_gun_stats(self, client):
        # initialize the clients spree stats
        client.setvar(self, self._clientvar_name, Guns())
        
    def get_gun_stats(self, client):
        # get the clients stats
        # pass the plugin reference first
        # the key second
        # the defualt value first
        
        if not client.isvar(self, self._clientvar_name):
            # initialize the default spree object
            # we don't just use the client.var(...,default) here so we
            # don't create a new SpreeStats object for no reason every call
            client.setvar(self, self._clientvar_name, Guns())
            
        return client.var(self, self._clientvar_name).value
        self.console.write('gw %s A%s-@' % (datclient, weapon))
        
    def someoneKilled(self, client, target, data=None):
        weap2 = self.get_gun_stats(client)
        if weap2.weapon==26:
            self.console.write('fraglimit 1')
            self.console.say('Congratulations %s You won this round!' % client.exactName)
            return False
            
        if (data[1] == self.console.UT_MOD_KNIFE):
            self.console.write('gh %s +100' % (client.cid))
        elif (data[1] == self.console.UT_MOD_KICKED):
            self.console.write('gh %s +100' % (client.cid))
        elif (data[1] == self.console.UT_MOD_BLED):
            item2 = random.choice((RandomGuns.items))
            self.console.write('gi %s %s' % (client.cid, item2))
            if item2=='D':
                item='Silencer'
            if item2=='E':
                item='Laser Sight'
            if item2=='C':
                item='Ultra Medkit'
            if item2=='A':
                item='Kevlar'
            if item2=='F':
                item='Helmet'
            client.message("^1Bleeding ^7kill ^1= ^7Random item: ^6%s" % item)
                
            RandomGuns.items.remove(item2)
            if RandomGuns.items == []:
                RandomGuns.items.insert(1, 'D')
                RandomGuns.items.insert(1, 'E')
                RandomGuns.items.insert(1, 'C')
                RandomGuns.items.insert(1, 'A')
                RandomGuns.items.insert(1, 'F')
        else:
            weap2.weapon += 1
            if weap2.weapon==0:
                weapon='B'
            elif weap2.weapon==1:
                weapon=self._guns[0]
            elif weap2.weapon==2:
                weapon=self._guns[0]
            elif weap2.weapon==3:
                weapon=self._guns[1]
            elif weap2.weapon==4:
                weapon=self._guns[1]
            elif weap2.weapon==5:
                weapon=self._guns[2]
            elif weap2.weapon==6:
                weapon=self._guns[2]
            elif weap2.weapon==7:
                weapon=self._guns[3]
            elif weap2.weapon==8:
                weapon=self._guns[3]
            elif weap2.weapon==9:
                weapon=self._guns[4]
            elif weap2.weapon==10:
                weapon=self._guns[4]
            elif weap2.weapon==11:
                weapon=self._guns[5]
            elif weap2.weapon==12:
                weapon=self._guns[5]
            elif weap2.weapon==13:
                weapon=self._guns[6]
            elif weap2.weapon==14:
                weapon=self._guns[6]
            elif weap2.weapon==15:
                weapon=self._guns[7]
            elif weap2.weapon==16:
                weapon=self._guns[7]
            elif weap2.weapon==17:
                weapon=self._guns[8]
            elif weap2.weapon==18:
                weapon=self._guns[8]
            elif weap2.weapon==19:
                weapon=self._guns[9]
            elif weap2.weapon==20:
                weapon=self._guns[9]
            elif weap2.weapon==21:
                weapon=self._guns[10]
                self.console.say('%s needs ^13^7 weapons to win!!' % client.exactName)
            elif weap2.weapon==22:
                weapon=self._guns[10]
            elif weap2.weapon==23:
                weapon=self._guns[11]
                self.console.say('%s needs ^12^7 weapons to win!!' % client.exactName)
            elif weap2.weapon==24:
                weapon=self._guns[11]
            elif weap2.weapon==25:
                weap2.weapon += 1
                self.console.write('bigtext "%s has the last weapon!: ^1Knife"' % client.exactName)
                weapon=''
            self.console.write('gw %s A%s-@' % (client.cid, weapon))
        
    def cmd_gun(self, data, client, cmd=None):
        weap2 = self.get_gun_stats(client)
        cmd.sayLoudOrPM(client, '^7You have ^2%s' % weap2.weapon)