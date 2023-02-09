<?php

class Message() {
  public $msg;
  public constructor($msg) {
    $this->val = $msg;
  }
}

$var = new Message('hello, world!');
var_dump($var);