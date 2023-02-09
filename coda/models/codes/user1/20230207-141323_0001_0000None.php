<?php

class Message {
  public $msg;
  public function constructor($msg) {
    $this->msg = $msg;
  }
}

$var = new Message('hello, world!');
var_dump($var);