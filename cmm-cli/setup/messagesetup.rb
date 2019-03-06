#!/usr/bin/ruby

#voicesetup.rb

#Declare requirements
require 'rubygems'
require 'plivo'
include Plivo
include Plivo::Exceptions


#Setup voice config
module Messagespoofsetup
   def Messagespoofsetup.create
#Menu to setup variables
         system "clear"
         prompt = TTY::Prompt.new
         spoofsource = prompt.ask('What is the number you want to pretend to be sending from? NOTE: All numbers must include country code! E.g. 61738921111 :')
         victimnumber = prompt.ask('What is the victim phone number you want to SMS? NOTE: All numbers must include country code! E.g. 61738921111 :')
         spoofmessage = prompt.ask('What is the message you would like to send? :', default: "Your message here")
		 
#Initiate Plivo Message
                api = RestClient.new(AUTH_ID, AUTH_TOKEN)
				begin
				response = api.messages.create(
				"#{spoofsource}",
				["#{victimnumber}"],
				"#{spoofmessage}",

  )
				rescue PlivoRESTError => e
				puts 'Exception: ' + e.message
				end

  end
end
