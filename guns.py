__author__  = 'LouK'
__version__ = '2.0'


import b3, random, time, thread, threading, re, string
import b3.events
import b3.plugin

#--------------------------------------------------------------------------------------------------
class RandomGuns:
    weapons                  = ['G', 'H', 'D', 'S', 'J', 'E', 'O', 'Q', 'I', 'N', 'F']
    items                  = ['D', 'E', 'C', 'A', 'F']

class GunsPlugin(b3.plugin.Plugin):
    requiresConfigFile = False
 
    def onLoadConfig(self):
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False
        
    def onStartup(self):
        self.registerEvent(b3.events.EVT_CLIENT_KILL)
    
    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_KILL: 
            self.someoneKilled(event.client, event.target, event.data)
        
    def someoneKilled(self, client, target, data=None):
        connections = client.connections
        if data[1] == self.console.UT_MOD_KNIFE:
            health = random.choice(('60', '20', '40', '80', '100', '70', '50')) 
            self.console.write('gh %s +%s' % (client.cid, health))
                
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1Knife ^7kill ^1= ^7Random Health: ^2+%s"' % (client.cid, health))
            else:
                client.message("^1Knife ^7kill ^1= ^7Random Health: ^2+%s" % (health))
 
        if data[1] == self.console.UT_MOD_GOOMBA:
            self.console.write('gw %s O 100 100' % (client.cid))
            self.console.write('gw %s Q 100 100' % (client.cid))
            self.console.write('gw %s I 100 100' % (client.cid))
            self.console.write('gw %s N 100 100' % (client.cid))
            self.console.write('gw %s F 100 100' % (client.cid))
            self.console.write('gw %s G 100 100' % (client.cid))
            self.console.write('gw %s H 100 100' % (client.cid))
            self.console.write('gw %s D 100 100' % (client.cid))
            self.console.write('gw %s S 100 100' % (client.cid))
            self.console.write('gw %s J 100 100' % (client.cid))
            self.console.write('gw %s E 100 100' % (client.cid))
            self.console.write('gw %s C 100 100' % (client.cid))
            self.console.write('gw %s B 100 100' % (client.cid))
                
            self.console.say( "%s ^1MADE A CURB STOMP^8!^3! ^7you won ^2ALL ^5WEAPONS ^7with ^4100 ^7ammo!!!" % client.exactName)

        if data[1] == self.console.UT_MOD_KNIFE_THROWN:
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
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1Throwing Knife ^7kill ^1= ^7Random item: ^6%s"' % (client.cid, item))
            else:
                client.message("^1Throwing Knife ^7kill ^1= ^7Random item: ^6%s" % item)
                
            RandomGuns.items.remove(item2)
            if RandomGuns.items == []:
                RandomGuns.items.insert(1, 'D')
                RandomGuns.items.insert(1, 'E')
                RandomGuns.items.insert(1, 'C')
                RandomGuns.items.insert(1, 'A')
                RandomGuns.items.insert(1, 'F')

        if data[1] == self.console.UT_MOD_DEAGLE:
            weap2 = random.choice((RandomGuns.weapons))
            self.console.write('gw %s %s' % (client.cid, weap2))
            if weap2=='N':
                weapon='^6Sr8'
            if weap2=='O':
                weapon='AK103'
            if weap2=='Q':
                weapon='^4NEGEV'
            if weap2=='F':
                weapon='^3UMP45'
            if weap2=='I':
                weapon='G36'
            if weap2=='G':
                weapon='^1HK69'
            if weap2=='H':
                weapon='LR300'
            if weap2=='D':
                weapon='^3Spas'
            if weap2=='S':
                weapon='M4A1'
            if weap2=='J':
                weapon='^6PSG1'
            if weap2=='E':
                weapon='^3MP5K'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^2Desert Eagle ^7kill ^1= ^5%s^7!"' % (client.cid, weapon))
            else:
                client.message("^2Desert Eagle ^7kill ^1= ^5%s^7!" % weapon)
                
            RandomGuns.weapons.remove(weap2)
            if RandomGuns.weapons == []:
                RandomGuns.weapons.insert(1, 'N')
                RandomGuns.weapons.insert(1, 'O')
                RandomGuns.weapons.insert(1, 'Q')
                RandomGuns.weapons.insert(1, 'F')
                RandomGuns.weapons.insert(1, 'I')
                RandomGuns.weapons.insert(1, 'G')
                RandomGuns.weapons.insert(1, 'H')
                RandomGuns.weapons.insert(1, 'D')
                RandomGuns.weapons.insert(1, 'S')
                RandomGuns.weapons.insert(1, 'J')
                RandomGuns.weapons.insert(1, 'E')

        if data[1] == self.console.UT_MOD_BERETTA:
            weap2 = random.choice((RandomGuns.weapons)) 
            self.console.write('gw %s %s' % (client.cid, weap2))
            if weap2=='N':
                weapon='^6Sr8'
            if weap2=='O':
                weapon='AK103'
            if weap2=='Q':
                weapon='^4NEGEV'
            if weap2=='F':
                weapon='^3UMP45'
            if weap2=='I':
                weapon='G36'
            if weap2=='G':
                weapon='^1HK69'
            if weap2=='H':
                weapon='LR300'
            if weap2=='D':
                weapon='^3Spas'
            if weap2=='S':
                weapon='M4A1'
            if weap2=='J':
                weapon='^6PSG1'
            if weap2=='E':
                weapon='^3MP5K'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^2Beretta ^7kill ^1= ^5%s^7!"' % (client.cid, weapon))
            else:
                client.message("^2Beretta ^7kill ^1= ^5%s^7!" % weapon)
            
            RandomGuns.weapons.remove(weap2)
            if RandomGuns.weapons == []:
                RandomGuns.weapons.insert(1, 'N')
                RandomGuns.weapons.insert(1, 'O')
                RandomGuns.weapons.insert(1, 'Q')
                RandomGuns.weapons.insert(1, 'F')
                RandomGuns.weapons.insert(1, 'I')
                RandomGuns.weapons.insert(1, 'G')
                RandomGuns.weapons.insert(1, 'H')
                RandomGuns.weapons.insert(1, 'D')
                RandomGuns.weapons.insert(1, 'S')
                RandomGuns.weapons.insert(1, 'J')
                RandomGuns.weapons.insert(1, 'E')

        if data[1] == self.console.UT_MOD_NEGEV:
            health2 = random.choice(('+50', '-30', '-40', '-75', '-50', '+75', '-100', '+100'))
            self.console.write('gh %s %s' % (client.cid, health2))
            if health2=='+50':
                health='^2+50'
            if health2=='+75':
                health='^2+75'
            if health2=='+100':
                health='^2+100'
            if health2=='-30':
                health='^1-30'
            if health2=='-40':
                health='^1-40'
            if health2=='-50':
                health='^1-50'
            if health2=='-75':
                health='^1-75'
            if health2=='-100':
                health='^1-100'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^4NEGEV ^7kill ^1= ^7Random Health: %s"' % (client.cid, health))
            else:
                client.message("^4NEGEV ^7kill ^1= ^7Random Health: %s" % health)

        if data[1] == self.console.UT_MOD_SPAS:
            weap2 = random.choice(('G', 'H', 'D', 'S', 'J', 'E', 'O', 'Q', 'I', 'N', 'F')) 
            ammo = random.choice(('100', '50', '40', '10', '20', '30', '60', '80', '70', '90', '255'))
            self.console.write('gw %s %s +%s' % (client.cid, weap2, ammo))
            if weap2=='N':
                weapon='^6Sr8'
            if weap2=='O':
                weapon='AK103'
            if weap2=='Q':
                weapon='^4NEGEV'
            if weap2=='F':
                weapon='^3UMP45'
            if weap2=='I':
                weapon='G36'
            if weap2=='G':
                weapon='^1HK69'
            if weap2=='H':
                weapon='LR300'
            if weap2=='D':
                weapon='^3Spas'
            if weap2=='S':
                weapon='M4A1'
            if weap2=='J':
                weapon='^6PSG1'
            if weap2=='E':
                weapon='^3MP5K'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^3Spas ^7kill ^1= ^7Random weapon & ammo^7: ^5%s ^4(+%s)"' % (client.cid, weapon, ammo))
            else:
                client.message("^3Spas ^7kill ^1= ^7Random weapon & ammo^7: ^5%s ^4(+%s) " % (weapon, ammo))

        if data[1] == self.console.UT_MOD_HK69:
            health2 = random.choice(('+50', '-30', '-40', '-75', '-50', '+75', '-100', '+100')) 
            self.console.write('gh %s %s' % (client.cid, health2))
            if health2=='+50':
                health='^2+50'
            if health2=='+75':
                health='^2+75'
            if health2=='+100':
                health='^2+100'
            if health2=='-30':
                health='^1-30'
            if health2=='-40':
                health='^1-40'
            if health2=='-50':
                health='^1-50'
            if health2=='-75':
                health='^1-75'
            if health2=='-100':
                health='^1-100'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1HK69 ^7kill ^1= ^7Random Health: %s"' % (client.cid, health))
            else:
                client.message("^1HK69 ^7kill ^1= ^7Random Health: %s" % health)
         
        if data[1] == self.console.UT_MOD_HK69_HIT:
            health2 = random.choice(('+50', '-30', '-40', '-75', '-50', '+75', '-100', '+100')) 
            self.console.write('gh %s %s' % (client.cid, health2))
            if health2=='+50':
                health='^2+50'
            if health2=='+75':
                health='^2+75'
            if health2=='+100':
                health='^2+100'
            if health2=='-30':
                health='^1-30'
            if health2=='-40':
                health='^1-40'
            if health2=='-50':
                health='^1-50'
            if health2=='-75':
                health='^1-75'
            if health2=='-100':
                health='^1-100'
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1HK69 ^7kill ^1= ^7Random Health: %s"' % (client.cid, health))
            else:
                client.message("^1HK69 ^7kill ^1= ^7Random Health: %s" % health)

        if data[1] == self.console.UT_MOD_SR8:
            nade = random.choice(('5', '8', '10', '12', '30', '15', '18', '12', '7', '20', '9', '50'))
            self.console.write('gw %s K +%s' % (client.cid, nade))
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^6Sr8 ^7kill ^1= ^7Random ^1HE Grenades^7: ^4(+%s)"' % (client.cid, nade))
            else:
                client.message("^6Sr8 ^7kill ^1= ^7Random ^1HE Grenades^7: ^4(+%s)" % nade)

        if data[1] == self.console.UT_MOD_PSG1:
            nade = random.choice(('5', '8', '10', '12', '30', '15', '18', '12', '7', '20', '9', '50'))
            self.console.write('gw %s K +%s' % (client.cid, nade))
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^6PSG1 ^7kill ^1= ^7Random ^1HE Grenades^7: ^4(+%s)"' % (client.cid, nade))
            else:
                client.message("^6PSG1 ^7kill ^1= ^7Random ^1HE Grenades^7: ^4(+%s)" % nade)


        if data[1] == self.console.UT_MOD_MP5K:
            self.console.write('gw %s C +15' % (client.cid))
                
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^3MP5K ^7kill ^1= ^3Desert Eagle^4(+15 Bullets)"' % (client.cid))
            else:
                client.message("^3MP5K ^7kill ^1= ^3Desert Eagle^4(+15 Bullets)")

        if data[1] == self.console.UT_MOD_UMP45:
            self.console.write('gw %s B +30' % (client.cid))
                
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^3UMP45 ^7kill ^1= ^5Beretta ^4(+30 bullets)"' % (client.cid))
            else:
                client.message("^3UMP45 ^7kill ^1= ^5Beretta ^4(+30 bullets)")
            
        if data[1] == self.console.UT_MOD_KICKED:
            health = random.choice(('60', '20', '40', '80', '100'))
            self.console.write('gh %s +%s' % (client.cid, health))

            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^6Boot ^7kill ^1= ^7Random Health: ^2+%s"' % (client.cid, health))
            else:
                client.message("^6Boot ^7kill ^1= ^7Random Health: ^2+%s" % health)
                
        if data[1] == self.console.UT_MOD_HEGRENADE:
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
                    
            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1HE Grenade ^7kill ^1= ^7Random item: ^6%s"' % (client.cid, item))
            else:
                client.message("^1HE Grenade ^7kill ^1= ^7Random item: ^6%s" % item)
                
            RandomGuns.items.remove(item2)
            if RandomGuns.items == []:
                RandomGuns.items.insert(1, 'D')
                RandomGuns.items.insert(1, 'E')
                RandomGuns.items.insert(1, 'C')
                RandomGuns.items.insert(1, 'A')
                RandomGuns.items.insert(1, 'F')
                
        if data[1] == self.console.UT_MOD_BLED:
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

            if connections < 10:
                self.console.write('sendclientcommand %s cp "For your ^1Bleeding ^7kill ^1= ^7Random item: ^6%s"' % (client.cid, item))
            else:
                client.message("^1Bleeding ^7kill ^1= ^7Random item: ^6%s" % item)
                
            RandomGuns.items.remove(item2)
            if RandomGuns.items == []:
                RandomGuns.items.insert(1, 'D')
                RandomGuns.items.insert(1, 'E')
                RandomGuns.items.insert(1, 'C')
                RandomGuns.items.insert(1, 'A')
                RandomGuns.items.insert(1, 'F')