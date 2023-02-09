<?php

class Message {
  public $msg;
  public function constructor($arg) {
    $this->msg = $arg;
  }
}

$var = new Message('hello, world!');
var_dump($var);