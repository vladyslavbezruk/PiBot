#!/bin/bash
id1="1002727" #IN01/1
id2="1002728" #IN01/2

site="https://schedule.sumdu.edu.ua/index/ical?id_grp=" #site

name1="schedule1.ics"
name2="schedule2.ics"

wget --cipher 'DEFAULT:!DH' "$site$id1" -O "$name1"
wget --cipher 'DEFAULT:!DH' "$site$id2" -O "$name2"

ical2json ./"$name1"
ical2json ./"$name2"
