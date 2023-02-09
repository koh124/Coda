<?php

class Message {
  public $msg;
  public function __construct($arg) {
    $this->msg = $arg;
  }
}

$var = new Message('hello, php!');
var_dump($var);