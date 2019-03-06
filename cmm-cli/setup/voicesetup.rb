#!/usr/bin/ruby

#voicesetup.rb

#Declare requirements
require 'tty-prompt'
require 'builder'
require 'rubygems'
require 'plivo'
require "net/http"

include Plivo
include Plivo::Exceptions

#Setup voice config
module Voicespoofsetup
   def Voicespoofsetup.create
#Menu to setup variables
         system "clear"
         ipifyaddress = Net::HTTP.get(URI("https://api.ipify.org"))
         prompt = TTY::Prompt.new
         spoofsource = prompt.ask('What is the number you want to pretend to be calling from? NOTE: All numbers must include country code! E.g. 61738921111 :')
         victimnumber = prompt.ask('What is the victim phone number you want to call? NOTE: All numbers must include country code! E.g. 61738921111 :')
         yournumber = prompt.ask('What is your number? You want to speak to them right? NOTE: All numbers must include country code! E.g. 61738921111 :')
         publicipaddress = prompt.ask('What is your public IP address? We need a public interface for the callback.', default: ipifyaddress)
#Write XML configuration file for Plivo callback
                open('www/voicespoof.xml', 'w') { |f|
                f << "<Response>"
                f << "<Dial callerId=\"#{spoofsource}\">"
                f << "<Number>#{victimnumber}</Number>"
                f << "</Dial>"
                f << "</Response>"
}

#Initiate Plivo Call
                api = RestClient.new(AUTH_ID, AUTH_TOKEN)
                        begin
                        response = api.calls.create(
                        "#{spoofsource}",
                        ["#{yournumber}"],
                        "http://#{publicipaddress}:8080/voicespoof.xml","GET",

  )

                        rescue PlivoRESTError => e
                        puts 'Exception: ' + e.message
                        end

  end
end
