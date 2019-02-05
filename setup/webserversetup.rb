#!/usr/bin/ruby

#webserversetup.rb

#Declare requirements
require 'un'

#Spawn process for web server
module Webserversetup
   def Webserversetup.create
         $webserver_pid = fork do
		 Signal.trap(3) { puts "Killing Web Server!"; exit }
                        original_stderr = $stderr.clone
                        original_stdout = $stdout.clone
                        $stderr.reopen(File.new('/dev/null', 'w'))
                        $stdout.reopen(File.new('/dev/null', 'w'))
                        Dir.chdir "./www"
                        httpd ./
                        end
end
end
