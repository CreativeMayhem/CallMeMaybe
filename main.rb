#! /usr/bin/env ruby

#main.rb

#Clear console
system "clear"

#Import script modules
require 'require_all'
require_rel 'setup'
require_rel 'config'
require 'tty-prompt'
#####################
begin

#Spawn Web Serber
Webserversetup.create

def mainmenu
puts <<-'EOF'
   ___      _ _
  / __\__ _| | |
 / /  / _` | | |
/ /__| (_| | | |
\____/\__,_|_|_|


  /\/\   ___
 /    \ / _ \
/ /\/\ \  __/
\/    \/\___|

                    _
  /\/\   __ _ _   _| |__   ___
 /    \ / _` | | | | '_ \ / _ \
/ /\/\ \ (_| | |_| | |_) |  __/
\/    \/\__,_|\__, |_.__/ \___|
              |___/

  .----------------.
 /    _H______H_    \@,
 \____/        \____/ @,
    /            \    `@
    |  LI LI LI  |    ,@
    |  LI LI LI  |   ,@'
    |  LI LI LI  |  ,@'
    |  LI LI LI  |@@'
    \            /'
     `----------'

EOF
#Setup TTY menu
prompt = TTY::Prompt.new
 menu1action = prompt.select("Select Action") do |menu|
  menu.choice 'Spoof Call', 1
  menu.choice 'Spoof SMS', 2
  menu.choice 'Brute Call Number Range', 3
  menu.choice 'Quit', 0
 end

#Action based on menu selection
if menu1action == 1
   if(File.exist?('www/voicespoof.xml'))
        voicespoofexistsmenu
   else
    Voicespoofsetup.create
    system "clear"
    puts "\n \n \n Call Initiated! \n \n \n"
    mainmenu
   end
  elsif menu1action == 2
   Messagespoofsetup.create
   system "clear"
   puts "\n \n \n Message Sent! \n \n \n"
   mainmenu
  elsif menu1action == 3
   puts "Not built yet!!"
   mainmenu
  elsif menu1action == 0
   system "clear"
   puts "Bye!"
   Process.kill(2,$webserver_pid)
#   Process.wait
   exit
 end

end
#####################

#Voice Setup menu if previous config exists
def voicespoofexistsmenu
#Setup TTY menu
prompt = TTY::Prompt.new
 voicespoofexistsmenu1action = prompt.select("Looks like you've done this before, overwrite previous settings?") do |menu|
  menu.choice 'Overwrite', 1
  menu.choice 'Cancel', 2
 end

#Action based on menu selection
if voicespoofexistsmenu1action == 1
   File.delete('www/voicespoof.xml')
   system "clear"
   puts "Configuration Cleared!"
   system "clear"
   Voicespoofsetup.create
   puts "Call Initiated!"
   mainmenu
  elsif voicespoofexistsmenu1action == 2
   system "clear"
   puts "Using Existing Config"
   mainmenu
 end

end
#####################
#Run menu
mainmenu

#Catch some errors
rescue SystemExit, Interrupt
  raise
rescue StandardError => e
   Process.kill(2,$webserver_pid)
   system "clear"
   puts "\n You kill me bro..."
rescue Exception => e
   Process.kill(2,$webserver_pid)
   system "clear"
   puts "\n You kill me bro..."
end
