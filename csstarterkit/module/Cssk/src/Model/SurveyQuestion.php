<?php

class Question {
    private $type;
    private $answers;

    function __construct($answersArray) {
        isset($answersArray) && is_array($answersArray) ? $this->answers = $answers : $this->answers = array();
    }


    // temp question:
    
}